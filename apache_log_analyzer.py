#!/usr/bin/env python3

# Author:  Rae Denruiter
# Email:  rlanderson1@wisc.edu
# Description:  "Analyze an Apache web log.  We will look to see if there is one trying to hack our website." 

from bs4 import BeautifulSoup

#Create a BeautifulSoup object to parse the HTML response
soup +BeautifulSoup(lookup_response, 'html.parser')

#Find the element containing information about the owner the owner of the IP address
owner_info = soup.find('div', class_='ip-info-item')

#Print the owner information
print("Owner Infromation:")
print(owner_info.get_text(strip=True))

import sys,subprocess,argparse,request

def IP(IPAddress):

    url = f"https://tools.keycdn.com/geo?host={IPAdress}"
    print("URL:", url) #Print the URL for verification
    response = requests.get(url)
    return response.text

#Call IPLookup function in main
lookup_response = IPLookup(top_ip)

#Takes in an apache log file and creates a summary of the top 5 ip address. Return the output
def IPAddressCount(apache_log_file_name):  #Arguement
    command = f"cat '{apache_log_file_name}' | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"  #Create a formated string w/o being hard codeded. Pythons know to use apache_log_name as it's arguement
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)  # pass in the command , stndout is able to access data,  and then Pythhon is going to open a diff. shell to run this process w/o make it a list
    return result.stdout.decode()   #Decode function. Return our results witht he stdout, we are grabbing the output of the above line, decode that and the pass that back

#Function that takes in an individual log entry and parses
def ParseLogEntry(logentry):

    #Split the string to get the return code
    apache_log_entry_items = logentry.split(' ')

    #Grabbing the correct elements of the apache log entry to output IP and return code
    ip_address = apache_log_entry_items[0]
    return_code = apache_log_entry_items[8]
    return [ip_address, return_code]

def main():
   
    #Create a description to show to the user
    parser = argparse.ArgumentParser(description="Analyze an Apache web log.")
    
    
    #Creating a new argument to pass in an apache log file name
    parser.add_argument('-f', '--filename', type=str, required=True, help="Enter an Apache File Name to process")
        
    #Grabbing a description to show the user
    args = parser.parse_args()
   

    #Create a description to show to the user
    description = "Analyze an Apache web log.  We will look to see if there is anyone trying to hack our website."

    print(description)   

    #Calling a function to get the summary information of our apache log file
    results = IPAddressCount(args.filename)
    top_ip_line = resultl.split('\n')[-2] # Get the second last lijne which contains the IP with the most request 
    top_ip = top_ip_line.split()[-1] # Get the last element from the splite line which is the IP address
    print("IP address with the most requests:", top_ip)
 
    #Print the first 250 characters of the response
    print("Response from IP Lookup:")
    print(lookup_response[:250])

    #Open a new file to output our analysis
    apache_log_analysis = open('apache_analysis.txt', 'w')
    
    apache_log_analysis.write(results)
    print(results)

    #Closing our analysis file
    apache_log_analysis.close()
    
if __name__ == "__main__":
    main()


   
