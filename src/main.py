import subprocess
import socket
import time
import threading
import sys
from termcolor import colored
from colorama import init
import pyfiglet  # For ASCII art

# Initialize colorama for cross-platform color support
init()

# Global variables to store test results
test_results = {}

# Spinner for process feedback (visual effect during background actions)
def spinner(stop_event):
    for symbol in ['|', '/', '-', '\\']:
        if stop_event.is_set():
            break
        print(f'\r{colored("Processing", "yellow")} {symbol}', end='', flush=True)
        time.sleep(0.1)

# Real-time logging for each process step
def log_process(action):
    print(colored(f"\nExecuting: {action}", "yellow"))
    time.sleep(0.5)  # Slight delay for user feedback

# Display a progress bar where each 5% increments
def progress_bar(progress, total, action="Progress"):
    percent = 100 * (progress / float(total))
    bar_length = 20  # Length of the progress bar in blocks
    block_progress = int(bar_length * (percent / 100))

    # Create a progress bar with filled and empty blocks
    bar = ('█' * block_progress).ljust(bar_length, ' ')
    colored_bar = colored(bar[:block_progress], 'white') + colored(bar[block_progress:], 'grey')
    
    sys.stdout.write(f'\r{colored(action, "yellow")}: |{colored_bar}| {percent:.2f}%')
    sys.stdout.flush()

# Display server details using speedtest-cli
def show_server_details():
    log_process("Retrieving server information from speedtest-cli...")

    try:
        result = subprocess.run(['speedtest-cli', '--list'], capture_output=True, text=True)
        server_list = result.stdout.splitlines()
        
        print(colored("Servers found:", "yellow"))
        for server in server_list[:5]:
            print(colored(server, "white"))

        print(colored("Selecting the best server...", "yellow"))
        time.sleep(0.5)

    except Exception as e:
        print(colored(f"Error retrieving server details: {str(e)}", "red"))

# Test download speed
def test_download_speed():
    log_process("Testing download speed...")

    try:
        total_progress = 100
        for i in range(total_progress):
            progress_bar(i + 1, total_progress, action="Downloading")
            time.sleep(0.02)

        result = subprocess.run(['speedtest-cli', '--simple'], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        if len(output_lines) >= 2:
            download_speed = output_lines[1].split()[1]
            test_results['Download Speed'] = f"{download_speed} Mbps"
            print(colored("\nDownload completed", "green"))
            print(colored(f"Download speed: {download_speed} Mbps", "white"))
        else:
            raise Exception("Unexpected output format from speedtest-cli")

    except Exception as e:
        print(colored(f"Error during download speed test: {str(e)}", "red"))
        test_results['Download Speed'] = "Error"

    return test_results['Download Speed']

# Test upload speed
def test_upload_speed():
    log_process("Testing upload speed...")

    try:
        total_progress = 100
        for i in range(total_progress):
            progress_bar(i + 1, total_progress, action="Uploading")
            time.sleep(0.02)

        result = subprocess.run(['speedtest-cli', '--simple'], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        if len(output_lines) >= 3:
            upload_speed = output_lines[2].split()[1]
            test_results['Upload Speed'] = f"{upload_speed} Mbps"
            print(colored("\nUpload completed", "green"))
            print(colored(f"Upload speed: {upload_speed} Mbps", "white"))
        else:
            raise Exception("Unexpected output format from speedtest-cli")

    except Exception as e:
        print(colored(f"Error during upload speed test: {str(e)}", "red"))
        test_results['Upload Speed'] = "Error"

    return test_results['Upload Speed']

# Ping and jitter testing
def test_ping_jitter(target="8.8.8.8"):
    log_process("Performing ping and jitter test...")
    pings = []

    try:
        for i in range(5):
            result = subprocess.run(['ping', '-c', '1', target], capture_output=True, text=True)
            if "time=" in result.stdout:
                response_time = float(result.stdout.split("time=")[1].split()[0])
                pings.append(response_time)
                print(colored(f"Ping {i+1}: {response_time:.2f} ms", "yellow"))
            else:
                print(colored(f"Ping {i+1} failed.", "red"))
            time.sleep(1)

        if pings:
            jitter = max(pings) - min(pings)
            avg_ping = sum(pings) / len(pings)
            test_results['Average Ping'] = f"{avg_ping:.2f} ms"
            test_results['Jitter'] = f"{jitter:.2f} ms"
            print(colored(f"Jitter: {jitter:.2f} ms", "white"))
            print(colored(f"Average Ping: {avg_ping:.2f} ms", "white"))
        else:
            raise Exception("No successful pings recorded.")

    except Exception as e:
        print(colored(f"Error during ping test: {str(e)}", "red"))
        test_results['Average Ping'] = "Error"
        test_results['Jitter'] = "Error"

    return test_results['Average Ping'], test_results['Jitter']

# Check network security (basic connectivity test)
def check_network_security():
    log_process("Checking network security...")

    try:
        external_ip = socket.gethostbyname("google.com")
        test_results['Network Security'] = f"Connected to {external_ip} (safe)"
        print(colored(f"Network connected to: {external_ip} (safe)", "green"))
    except socket.error as err:
        test_results['Network Security'] = "Connection Failed"
        print(colored(f"Network error: {err}", "red"))

    return test_results['Network Security']

# Print the test results
def print_test_results():
    print("\n" + colored("--- Final Test Results ---", "blue"))
    for key, value in test_results.items():
        print(f"{key}: {value}")

# Main function to run the network test
def perform_network_test():
    print("\n" + colored("Network Test - Made by LSMB", "blue") + "\n")

    stop_spinner = threading.Event()
    spinner_thread = threading.Thread(target=spinner, args=(stop_spinner,))
    spinner_thread.start()

    # Execute tests
    show_server_details()
    test_download_speed()
    test_upload_speed()
    test_ping_jitter()
    check_network_security()

    stop_spinner.set()
    spinner_thread.join()

    print_test_results()

# Command handler
def handle_command(command):
    command = command.lower()

    if command == "start":
        perform_network_test()
    elif command == "stop":
        print(colored("The test is currently not running.", "yellow"))
    elif command == "results":
        print_test_results()
    elif command == "help":
        print(colored("""
Available Commands:
  start      - Start the network test.
  stop       - Stop the network test.
  results    - Print the test results.
  help       - Show available commands.
  exit       - Exit the program.
        """, "cyan"))
    elif command == "exit":
        print(colored("Goodbye!", "green"))
        sys.exit(0)
    else:
        print(colored("Unknown command. Type 'help' to see available commands.", "red"))

# Main function to handle user input
def start_network_test():
    print(colored("Network Test Script - Made by LSMB", "cyan"))

    banner = pyfiglet.figlet_format("LSMB")
    print(colored(banner, "cyan"))

    print(colored("Type 'help' to see all available commands.", "cyan"))

    while True:
        command = input(colored("\nCommand: ", "cyan"))
        handle_command(command)

if __name__ == "__main__":
    start_network_test()
