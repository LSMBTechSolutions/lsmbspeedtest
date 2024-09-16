# LSMB Speed Test

## Table of Contents
1. [Introduction]
2. [Features]
3. [System Requirements]
4. [Installation]
5. [Usage Instructions]
6. [Understanding the Results]
7. [Troubleshooting]
8. [Code Breakdown]
9. [Contact and Support]
10. [Contributing to the Project]
11. [License]

## Introduction
LSMB Speed Test is a network utility designed to measure internet connection speed, check network stability through ping and jitter tests, and perform basic network security checks. The tool provides real-time feedback and logs each process step for enhanced user experience.

## Features
- Download Speed Test: Accurately measures your network's download speed using speedtest-cli and displays the result in Mbps.
- Upload Speed Test: Measures your network's upload speed and provides results in Mbps, helping assess the quality of your internet connection.
- Ping Test: Calculates the latency in milliseconds, showing how quickly your network can send and receive data.
- Jitter Test: Measures the variation in ping times, providing insight into the stability of your connection.
- Network Security Check: Verifies your network's connection to external servers and checks for potential issues with network security.
- Real-Time Process Feedback: Displays a spinner during test execution and a progress bar to track download and upload tests.
- Server Details Display: Fetches a list of available speed test servers and selects the best one based on location for more accurate results.
- Cross-Platform Color Support: Terminal output uses colored text for better clarity and enhanced user experience across different platforms.
- Command-Based Operation: Simple command-line interface for starting tests, stopping them, viewing results, and getting help.
- ASCII Art Banner: Adds a personalized ASCII art header with pyfiglet to give the interface a visually engaging look.

## System Requirements
- Python 3.x: Ensure Python version 3.x is installed on your system.
- Required Python Packages:
  - termcolor: For colored terminal output.
  - colorama: Provides cross-platform color support in the terminal.
  - pyfiglet: Used to generate ASCII art banners.
  - speedtest-cli: The core tool for performing internet speed tests.
- Compatible with Linux, macOS, and Windows operating systems.
- Internet connection required for performing the speed tests.

## Installation
- Clone the Repository:
  - git clone https://github.com/LSMBGlobalSolutions/lsmbspeedtest.git
- Navigate to the Project Directory:
  - cd lsmbspeedtest
- Install Required Dependencies:
  # pip3 install -r requirements.txt
- Run the Application:
  - python3 main.py

## Usage Instructions
- To start the speed test, run:
  - python3 main.py
- Available Commands:
  - start: Run the full speed test.
  - stop: Stop any running tests.
  - results: View the test results.
  - help: Show available commands.
  - exit: Exit the program.

## Understanding the Results
- Download Speed: Displays the internet's download speed in Mbps.
- Upload Speed: Shows the internet's upload speed in Mbps.
- Ping: Measures network latency in milliseconds (ms), indicating the time taken for data to travel to and from a server.
- Jitter: Calculates the variation in ping times, reflecting the stability of the network connection.
- Network Security: Displays whether the network is securely connected to an external server and shows the external IP address.

## Troubleshooting
- Ensure Python 3.x is installed on your system.
- Verify that all required packages are installed:
  - termcolor, colorama, pyfiglet, speedtest-cli.
- Check your internet connection if speed tests fail or give unexpected results.
- Run the script with administrator privileges if necessary, especially on Windows.
- If the application crashes, review the error messages for missing dependencies or permission issues.

## Code Breakdown
- main.py: Contains the core logic of the network speed test tool.
- Spinner: Provides visual feedback while processes are running.
- Progress Bar: Displays real-time progress for download and upload tests.
- show_server_details: Retrieves and displays available speed test servers.
- test_download_speed: Measures and reports the download speed of the internet connection.
- test_upload_speed: Measures and reports the upload speed of the internet connection.
- test_ping_jitter: Performs a ping and jitter test to evaluate network latency and stability.
- check_network_security: Verifies the network’s security by checking the external IP connection.
- print_test_results: Outputs a summary of all the test results.
- handle_command: Processes user commands such as start, stop, and results.

## Contact and Support
- For any issues or inquiries, please contact:
  - LSMB Global Solutions Corp
  - Email: lsmb_app_developer@proton.me
- Visit our GitHub repository for updates and contributions:
  - https://github.com/LSMBGlobalSolutions/lsmbspeedtest

## Contributing to the Project
- Contributions are welcome! Please follow these steps:
  - Fork the repository on GitHub.
  - Create a new branch for your feature or bug fix.
  - Commit your changes with clear and descriptive messages.
  - Submit a pull request, explaining your changes and improvements.
- For major changes, please open an issue first to discuss what you would like to change.

## License
- This project is licensed under the Apache License 2.0.
- You may obtain a copy of the License at:
  - http://www.apache.org/licenses/LICENSE-2.0
- Unless required by applicable law or agreed to in writing, software distributed under this License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
