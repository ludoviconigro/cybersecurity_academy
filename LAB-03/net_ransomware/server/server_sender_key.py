import socketserver     # Provides a framework for writing network servers
import subprocess       # Allows execution of external system commands (e.g., OpenSSL)
import os               # Provides functions to interact with the file system

class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Step 1: Receive encrypted data from the client
        encrypted_data = self.request.recv(4096)  # Reads up to 4096 bytes from the socket
        print("Encrypted data received")

        # Step 2: Save the encrypted data to a binary file
        with open("cipher.bin", "wb") as f:
            f.write(encrypted_data)

        try:
            # Step 3: Convert the binary file to base64 format using OpenSSL
            # This step is often unnecessary unless required by a specific processing constraint
            subprocess.run(["openssl", "base64", "-in", "cipher.bin", "-out", "cipher64.txt"], check=True)
            print("Binary file converted to base64")

            # Step 4: Decode the base64 back into binary format
            subprocess.run(["openssl", "base64", "-d", "-in", "cipher64.txt", "-out", "cipher64.bin"], check=True)
            print("Base64-decoded file written as binary")

            # Step 5: Decrypt the binary file using RSA with OAEP padding
            subprocess.run([
                "openssl", "pkeyutl", "-decrypt",
                "-inkey", "pub_priv_pair.key",         # Private key used for decryption
                "-in", "cipher64.bin",                 # Encrypted input
                "-out", "plainD.txt",                  # Decrypted output
                "-pkeyopt", "rsa_padding_mode:oaep"    # Specify OAEP as padding mode
            ], check=True)
            print("Decryption successful")

            # Step 6: Read the decrypted content and send it back to the client
            with open("plainD.txt", "rb") as f:
                decrypted_data = f.read()
                self.request.sendall(decrypted_data)
            print("Decrypted file sent to client")

        except subprocess.CalledProcessError as e:
            # Handle errors raised during OpenSSL command execution
            print("An error occurred while running OpenSSL:", e)

        finally:
            # Step 7: Clean up temporary files to avoid cluttering the file system
            for filename in ["cipher.bin", "cipher64.txt", "cipher64.bin", "plainD.txt"]:
                if os.path.exists(filename):
                    os.remove(filename)

if __name__ == "__main__":
    HOST, PORT = "", 8082  # Bind to all interfaces on TCP port 8082
    with socketserver.TCPServer((HOST, PORT), ClientHandler) as tcpServer:
        print("Server listening on port", PORT)
        try:
            tcpServer.serve_forever()  # Start handling incoming client connections
        except KeyboardInterrupt:
            print("\nServer interrupted by user")
        except Exception as e:
            print("Server encountered an error:", e)
