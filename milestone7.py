#!/usr/bin/env python3

# Importing necessary modules
import re

# Step 2: Define the ParseLogEntry function
def ParseLogEntry(log_entry):
    """
    Parse Apache log entry to extract IP address and Return Code.
    
    Args:
    log_entry (str): Apache log entry string.
    
    Returns:
    tuple: IP address and Return Code extracted from the log entry.
    """
    # Regular expression pattern to extract IP address and Return Code
    pattern = r'(\d+\.\d+\.\d+\.\d+)\s-\s-\s\[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}\]\s"\w+\s\S+\s\S+"\s(\d{3})\s\d+'
    
    # Using regular expression to find IP address and Return Code
    match = re.match(pattern, log_entry)
    
    if match:
        ip_address = match.group(1)
        return_code = match.group(2)
        return ip_address, return_code
    else:
        return None, None

# Step 1: Define the main function
def main():
    # Sample Apache log entries
    log_entries = [
        '192.168.1.1 - - [20/Feb/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234',
        '127.0.0.1 - - [20/Feb/2024:10:35:12 +0000] "POST /submit_form HTTP/1.1" 404 5678'
    ]
    
    # Step 3: Using the new function in the main function
    for log_entry in log_entries:
        ip_address, return_code = ParseLogEntry(log_entry)
        print("IP Address:", ip_address)
        print("Return Code:", return_code)
        print()  # Adding a newline for clarity

# Step 1: Running the main function if the script is run directly
if __name__ == "__main__":
    main()
