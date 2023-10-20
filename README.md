# Done by Anurag Patil - https://www.linkedin.com/in/anurag-patil-2a9b0022a/
# AccessWiz - A Remote Access Trojan (RAT)

## `AccessWiz - A Remote Access Trojan (RAT)` is a `Post Exploitation` tool for Information Gathering and Further Enumeration.

**Note:** **The Server Side (Victim Machine) code is specifically tailored for Linux based OS only and should be run using `ROOT PRIVILEGE` only**

**Note:** **To make the OS not ask for `ROOT PASSWORD` after default timeout (15 minutes) follow the below steps**

    1. On the terminal run: "sudo visudo"
    2. Add the following line to the sudoers list: "Your_Username ALL = NOPASSWD : ALL" (Replace Your_Username with your real User Name)

## Introduction

This project implements a Remote Access Trojan (RAT) system consisting of both client and server components. A RAT allows remote control of a target computer, enabling various interactions and data exchange with the target system. This README provides an overview of the project, including its functionalities, components, and instructions for use.

## Features
    1. No Dependency Issues: No need to worry about downloading dependencies, the client side code checks if the required dependencies exist, if not it downloads them automatically.
    
    2. Client-Server Architecture: The RAT consists of both client and server components for remote control.
    
    3. Menu-Driven Interaction: The server provides a menu-driven interface for easy interaction with the client.
    
    4. File Transfer: The system supports file transfer between the server and client.
    
    5. Error Handling: Robust error handling for various scenarios ensures a smooth experience.


## Components

### Client Side
The client-side code (`client.py`) is intended to be run on the target machine, providing a gateway for the hacker (server) to interact with the compromised system. Key functionalities of the client-side code include:

    1. No Dependencie Issues: Downloads missing dependencies on client machine automatically.
    
    2. Capture Screenshot: Takes a screenshot of the target system and sends it to the server.
    
    3. Retrieve Linux Wi-Fi Passwords: Retrieves saved Wi-Fi passwords from the target Linux system and sends them to the server.
    
    4. Get Linux Password Hashes: Retrieves password hashes from the target Linux system and sends them to the server.
    
    5. Get Directory and File List: Generates a list of all directories and files on the target system and sends it to the server.
    
    6. Get System Information: Gathers system information from the target system (e.g., OS version, hardware details) and sends it to the server.
    
    7. Get Geolocation Information: Retrieves geolocation information of the target system and sends it to the server.
    
    8. Download File: Allows the server to request specific files from the client.
    
    9. Upload File: Accepts files from the server and stores them on the client.

### Server Side
The server-side code (`server.py`) acts as the hacker's control center, allowing them to connect to compromised clients and perform various actions. Key functionalities of the server-side code include:

    1. Listening for Connections: Listens for incoming client connections on a specified IP address and port.
    
    2. Menu-Driven Interaction: Offers a menu of options for the hacker to choose from, including capturing screenshots, retrieving data, and managing files.
    
    3. File Transfer: Handles the sending and receiving of files between the server and client.
    
    4. Error Handling: Provides error handling for various scenarios, such as invalid file paths and failed operations.

## Usage

1. **Server Setup**:
   - Run the `server.py` script on the attacker's machine.
   - The server listens all IP address and port (8783) (0.0.0.0:8783) for all incoming client connections.

2. **Client Setup**:
   - Deploy the `client.py` script on the target machine.
   - The client connects to the server's IP address and port to establish a connection.

3. **Interaction**:
   - The server offers a menu-driven interface for the attacker to choose actions.
   - The client executes the requested actions and sends back the results to the server.

4. **File Transfer**:
   - The server can request specific files from the client using the "Download File" option.
   - The server can upload files to the client using the "Upload File" option.

5. **Termination**:
   - The attacker can exit the RAT at any time using the "Exit" option.

## Why Choose This RAT Project?

The Remote Access Trojan (RAT) project offers several advantages for those interested in learning about Ethical Hacking and Network Security:

- **Educational Purpose**: This project is primarily designed for educational purposes, allowing individuals to understand the concepts and techniques involved in remote access and control.

- **Hands-On Experience**: Users can gain practical, hands-on experience in setting up a client-server architecture, establishing connections, and interacting with a remote system.

- **Understanding Security**: By exploring the functionalities of this RAT, users can better understand security risks and vulnerabilities associated with such software, helping them develop defensive strategies.

- **Customization**: This RAT project can serve as a foundation for building more complex and customized remote access tools, tailored to specific learning objectives.

- **Community Contribution**: The open-source nature of this project allows users to contribute, collaborate, and enhance the tool's functionality within the ethical hacking community.

## Stay Responsible:

With great power comes great responsibility. AccessWiz is a powerful tool that should be used responsibly and ethically. Ensure you have the proper authorization before using this tool. Use CipherNova for legitimate purposes, such as to gain Hands-On Experience, security enhancement, or educational exploration. Adhere to ethical standards and legal regulations when utilizing this tool.

Feel free to explore and contribute to the CipherNova project, and safeguard your data with advanced encryption techniques!

**Note:** For a detailed explanation of each function and its usage, refer to the code documentation and comments.

## Disclaimer

**Important**: The use of `AccessWiz - A Remote Access Trojan (RAT)` for unauthorized access to computer systems is illegal and unethical. This project is purely educational and should be used only for legal and ethical purposes, such as learning about eithical hacking and network security. Unauthorized use of this software for malicious purposes is strictly prohibited. The creators and contributors of this tool hold no responsibility for any misuse or unauthorized activities.
