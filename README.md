Nmap Automation Tool
Overview
The Nmap Automation Tool is a graphical user interface (GUI) developed in Python using the Tkinter library. It provides an easy and interactive way to perform various Nmap scans on a target IP address or hostname. Users can select from a range of scan types, execute them with a click of a button, and save the scan results to a file.

Features
Stealth Scan (SYN Scan)
Aggressive Scan
All Port Scan
Specific Port Scan
TCP Scan
UDP Scan
Service Version Detection
Operating System Detection
Ping Scan
NULL Scan
MSSQL Scan
Script Scan
IPv6 Scanning
List Scan
The tool allows you to:

Specify a target IP address or hostname.
Select from different Nmap scan types.
View the output directly within the application.
Save scan results to a text file.
Prerequisites
Ensure that the following dependencies are installed:

Python 3.x
Tkinter (included with most Python installations)
Nmap (Installable via package managers like apt, brew, or chocolatey)
Installation
Clone this repository:

git clone https://github.com/yourusername/nmap-automation-tool.git
Navigate to the project directory:

cd nmap-automation-tool
Ensure that Nmap is installed on your system. You can verify by running:

nmap --version
Run the application:

python3 nmap_automation_tool.py
Usage
Launch the application by running the Python script.

In the GUI:

Enter the target IP address or hostname.
Specify any required ports (for the Specific Port Scan).
Choose the desired scan type by clicking on one of the scan buttons.
The output will be displayed in the text area.
You can save the scan report to a file by following the prompts.
Saving Scan Results
After performing a scan, you will be prompted to save the scan results. You can choose the file location and name, and the results will be saved in a .txt file.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
