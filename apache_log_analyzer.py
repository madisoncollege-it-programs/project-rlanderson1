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
#user_input = input("Would you like to continue? (y/n): ") 
#print(f"User input received: {user_input}")
#Setting the apache log entry to the standard format with an example log entry

apache_log = """111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"""

print(apache_log)
#take the apache log and split it and then list the four lines
apache_log_analyzer = apache_log.split('\n')
#print(apache_log)
#Create a loop through the list and print out each line
for entry in apache_log_analyzer:
    print(entry)

    #Grabbing the first 16 characters of the log entry which is the IP address
    ip_address = apache_log[0:15:1]
    #print(f"IPAddress is: {ip_address}")
    print(f"Log request from: {ip_address:*^22s}")
    #Split the string to get the return code
    apache_log_analyzer_items = apache_log.split(' ') 
    return_code = apache_log_analyzer_items[8]
    print(f"Return Code: {return_code}")

