#!/usr/bin/env python3
""" 
apache_log_analyzer.py

# Author:  Rae Denruiter
# Email:  rlanderson1@wisc.edu
# Description:  "Analyze an Apache web log.  We will look to see if there is one trying to hack our website." 
"""

import sys
import subprocess

def ParseLogEntry(logentry):

    #Split the string to get the return code
    apache_log_entry_items = logentry.split(' ') 

    #Grabbing the correct elements of the apache log entry to output IP and return code
    ip_address = apache_log_entry_items[0]
    return_code = apache_log_entry_items[8]
    return [ip_address, return_code]

def IPAddressCount(apache_log_analyzer):
    #Construct the command string
    command = f"cat {apache_log_analyzer} | cut -d ' ' -f1 | sort | uniq -c | sort -n | tail -n5"

    #Run the command using subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    #Return the resulting string
    return result.stdout


def main():

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

            #Setting the apache log file name
            apache_log_analyzer = "m5-access.log"

            #Call the  IPAddressCount function
            result = IPAddressCount(apache_log_analyzer)

            #Print the results to the screen
            print(result)

            #Write the results to the apache_analysisd.txt file
            with open("apache_analysis.txt", "w") as file:
                file.write(result)
            
        else:
            print("You chose not to continue.  Exiting the program...")

    else:
        print("Invalid response.  Exiting the program.")

if __name__ == "__main__":
    main()


   



   


