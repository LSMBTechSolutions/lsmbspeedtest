import time
import sys
from termcolor import colored

# Function to display a spinner for feedback
def spinner(stop_event):
    for symbol in ['|', '/', '-', '\\']:
        if stop_event.is_set():
            break
        print(f'\r{colored("Processing", "yellow")} {symbol}', end='', flush=True)
        time.sleep(0.1)

# Function to log each process step
def log_process(action):
    print(colored(f"\nExecuting: {action}", "yellow"))
    time.sleep(0.5)  # Slight delay for user feedback

# Function to display a progress bar
def progress_bar(progress, total, action="Progress"):
    percent = 100 * (progress / float(total))
    bar_length = 20  # Length of the progress bar in blocks
    block_progress = int(bar_length * (percent / 100))

    # Create a progress bar with filled and empty blocks
    bar = ('█' * block_progress).ljust(bar_length, ' ')
    colored_bar = colored(bar[:block_progress], 'white') + colored(bar[block_progress:], 'grey')
    
    sys.stdout.write(f'\r{colored(action, "yellow")}: |{colored_bar}| {percent:.2f}%')
    sys.stdout.flush()

# Function to print final test results in a neat format
def print_test_results(test_results):
    print("\n" + colored("--- Final Test Results ---", "blue"))
    for key, value in test_results.items():
        print(f"{key}: {value}")
