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
apache_log_analyzer = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'
# print(apache_log_analyzer)
ip_address = apache_log_analyzer.split()[0]
# print(f"Log request from: ***{ip_address}****")
split_entry = apache_log_analyzer.split()
# print("Type of object after splitting: ", type(split_entry))
return_code = split_entry[8]
print(f"Return Code: {return_code}")