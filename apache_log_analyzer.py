#!/usr/bin/env python3
""" 
apache_log_analyzer.py

# Author:  Rae Denruiter
# Email:  rlanderson1@wisc.edu
# Description:  This script is part of the course project.  It automates the process of cloning a repository, updating README.md, 
# and interesting with the user to continue or exit the 
# program.
"""

# Step 2 - Add Output
output_message = "This script automates the process of cloning a course repository, updating README.md, and interacting with the user."

print(output_message)

# Step 3 - Ask for Input
user_input = input("Would you like to continue? (y/n): ") 
print(f"User input received: {user_input}")
#Setting the apache log entry to the standard format with multiple log entries
"""apache_log = 111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"""

apache_log_file = open("m5-access.log", "r")

apache_log = apache_log_file.read()


##Splitting the entire log into individual log entries (1 per line)
apache_log_entries = apache_log.split('\n')
#print(apache_log_entries)
apache_log_analysis = open('apache_analysis.txt', 'w')
#Looping through each log entry in my list of log enteries
for entry in apache_log_entries:
    
    #Grabbing the first 16 charaters of the log entry which is the IP Address
    #ip_address = entry[0:15:1]
    #Split the string to get the return code
    apache_log_entry_items = entry.split(' ') 
    ip_address = apache_log_entry_items[0]
    return_code = apache_log_entry_items[8]
    summary = (f"{ip_address} - {return_code}")
    #print(f"IPAddress is: {ip_address}")
    print(summary)
    apache_log_analysis.write(summary + "\n")
import sys

if user_input in ['y', 'yes', 'yeah']:
    #Open the Apache log file
    with open("m5-access.log", 'r') as file:
    #Read each line in the file
        for line in file:
            #Extract the return code from the log entry
            retrun_code = int(line.split()[8])
            #Check for errors
            #if return_code >= 400:
                #Print error codes >= 400 to the screen
                #print(return_code)
            #Check for server errors (500 level or higher)
            if return_code >= 500:
                #Write output to file for server errors (500 level or higher)
                with open('error_log.txt', 'a') as error_file:
                    error_file.wwrite(line)
else:
    print("You chose not to continue.")


apache_log_analysis.close()


