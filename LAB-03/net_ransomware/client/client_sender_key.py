import socket       # Used for TCP/IP communication
import sys          # Used to access command-line arguments and exit gracefully

def get_server_address():
    """
    Prompts the user to enter a valid server IP address and port.
    Repeats until valid input is provided.
    """
    while True:
        try:
            # Ask the user to input the server IP address
            ip = input("Enter the server IP address: ").strip()
            if not ip:
                print("IP address cannot be empty.")
                continue

            # Ask the user to input the port number
            port_input = input("Enter the server port number: ").strip()
            if not port_input.isdigit():
                print("Port must be a number.")
                continue

            port = int(port_input)
            if not (0 < port < 65536):
                print("Port must be in range 1–65535.")
                continue

            # Return the validated IP and port as a tuple
            return (ip, port)
        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C during input
            print("\nUser interrupted input. Exiting.")
            sys.exit(1)

def main():
    """
    Main client routine:
    - Reads the encrypted file (cipher.bin)
    - Connects to the specified server
    - Sends the file
    - Receives the decrypted file in response
    """
    # Check if IP and port are provided via command-line arguments
    if len(sys.argv) == 3:
        server_ip = sys.argv[1]
        try:
            server_port = int(sys.argv[2])
            if not (0 < server_port < 65536):
                raise ValueError
            server_address = (server_ip, server_port)
        except ValueError:
            print("Invalid port number in arguments.")
            server_address = get_server_address()
    else:
        # If not provided, prompt the user for input
        server_address = get_server_address()

    # Attempt to read the encrypted file (cipher.bin) from the local filesystem
    try:
        with open("cipher.bin", "rb") as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        print("Error: 'cipher.bin' not found.")
        return

    # Attempt to connect to the server and send the encrypted data
    try:
        with socket.create_connection(server_address) as sock:
            print(f"Connected to server {server_address[0]}:{server_address[1]}")

            # Send the entire encrypted file to the server
            sock.sendall(encrypted_data)
            print("File 'cipher.bin' sent to the server")

            # Receive the decrypted file data in chunks
            decrypted_data = b""
            while True:
                part = sock.recv(4096)  # Read in chunks of 4096 bytes
                if not part:
                    break              # Exit loop when no more data is received
                decrypted_data += part

            print("Decrypted file received from the server.")

            # Write the received decrypted data to a local file (plainD.txt)
            with open("plainD.txt", "wb") as f:
                f.write(decrypted_data)
            print("File 'plainD.txt' saved locally.")

    except ConnectionRefusedError:
        # Handle the case where the server is not accepting connections
        print("Error: Connection refused. Ensure the server is running and reachable.")
    except Exception as e:
        # Catch and display any other unexpected error
        print(f"Error during connection or data transfer: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
