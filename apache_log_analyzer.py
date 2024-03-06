#!/usr/bin/env python3
""" 
apache_log_analyzer.py

# Author:  Rae Denruiter
# Email:  rlanderson1@wisc.edu
# Description:  "Analyze an Apache web log.  We will look to see if there is one trying to hack our website." 
"""

import sys

#Create a description to show to the user
description = "Analyze an Apache web log.  We will look to see if there is anyone trying to hack our website"

print(description)

#Arguement statement
if len(sys.argv) > 1:
#Argument list
        user_response = sys.argv[1]

    #Ask the user if they want to continue
 
#If there isn't an argument
else:
    user_response = input("Would you like to continue?  (y or n)")

acceptable_responses = ['y','yes', 'yeah']

if user_response.lower() in acceptable_responses:

 #Make a one by one instead 
    if user_response.lower():
        # == 'y' or user_response.lower() == 'yes' or user_response.lower() == 'yeah':

        #Make it a list
        #print(f"Your response is ... (user response):")

        #Setting the apache log entry to the standard format with multiple log entries
        """apache_log = 111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
        111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
        111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
        111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"""
        #Opening in the log file we want to process
        apache_log_file = open("m5-access.log", "r")
        #Reading in the log file into one large string
        apache_log = apache_log_file.read()


        ##Splitting the entire log into individual log entries (1 per line)
        apache_log_entries = apache_log.split('\n')
        #print(apache_log_entries)

        #Open a new file to output our analysis
        apache_log_analysis = open('apache_analysis.txt', 'w')
        apache_log_summary = {}

        #Looping through each log entry in my list of log enteries
        for entry in apache_log_entries:    
            #ip_address = entry[0:15:1]
            #Split the string to get the return code
            apache_log_entry_items = entry.split(' ') 

            #Grabbing the correct elements of the apache log entry to output IP and return code
            ip_address = apache_log_entry_items[0]
            return_code = apache_log_entry_items[8]

            #Create dictionary entries for the IP addresses in my log file
            if ip_address in apache_log_summary:
                apache_log_summary[ip_address] += 1
            else:
                apache_log_summary[ip_address] = 1
            
            #Summarizing information to print to the screen and save to a file
            summary = f"{ip_address} - {return_code}"
            #print(f"IPAddress is: {ip_address}")

            if return_code >= '400':
                print(summary)
            #if return_code >= '500':    
                #apache_log_analysis.write(summary + "\n")
                
        #print(apache_log_summary) 
        #Loop through my summary ip info and print out the high occuring IP address
        for ip in apache_log_summary:
            if apache_log_summary[ip] >= 5:
                apache_log_analysis.write(f"{ip} called website {apache_log_summary[ip]} times.\n")

        #Closing our analysis file
        apache_log_analysis.close()

else:
    print("You chose not to continue.  Exiting the program...")


   



   


