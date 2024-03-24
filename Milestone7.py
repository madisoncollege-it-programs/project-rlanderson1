#!/usr/bin/env python3
def ParseLogEntry(apache_log_analyzer):
    #Split the log entry into items
    items = apache_log_analyzer.split()

    return ip_address, return_code

def main():
    
    #print("Functions in Python.")

    #apache_log_analyzer = input("Enter Apache log analyzer entry: ")
    

    #Call the ParseLogEntry function and unpack the returned values
    ip_address, return_code = ParseLogEntry(apache_log_analyzer)

    #Print the extracted IP address and teturn Code
    #print("IP Address:", ip_address)
    #print("Return Code:", return_code)

if __name__ == "__main__":
     main()