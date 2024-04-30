#!/usr/bin/env python3

# Author:  Rae Denruiter
# Email:  rlanderson1@wisc.edu
# Description:  "Analyze an Apache web log.  We will look to see if there is one trying to hack our website." 

import subprocess,argparse,requests,json

#Function to call a website to get more information about an IP address
def IPLookup(ip_address):

    #URL to call to lookup IP
    url = f"https://virustotal.com/api/v3/ip_addresses/{ip_address}"  #API formate
    print(url) #Print the URL for verification

    credfile = open('/home/student/.credentials-vt', 'r')
    credentials = credfile.readlines()
    api_key = credentials[0].split('=')[1].strip()

    print(f"API Key: {api_key}")

    header = {}
    header['x-apikey'] = api_key
    
    #Make a requests to the specified URL
    response = requests.get(url,headers=header)
    return response.text

#Takes in an apache log file and creates a summary of the top 5 ip address. Return the output
def IPAddressCount(apache_log_file_name):  #Arguement
    command = f"cat {apache_log_file_name} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"  #Create a formated string w/o being hard codeded. Pythons know to use apache_log_name as it's arguement
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)  # pass in the command , stndout is able to access data,  and then Pythhon is going to open a diff. shell to run this process w/o make it a list
    return result.stdout.decode()   #Decode function. Return our results witht he stdout, we are grabbing the output of the above line, decode that and the pass that back

#Function that takes in an individual log entry and parses (set up to include any arguments that we end up adding to this script)
def ParseLogEntry(logentry):

    #Split the string to get the return code
    apache_log_entry_items = logentry.split(' ')

    #Grabbing the correct elements of the apache log entry to output IP and return code
    ip_address = apache_log_entry_items[0]
    return_code = apache_log_entry_items[8]
    return [ip_address, return_code]

def main():
   
    # Create a description to show to the user
    parser = argparse.ArgumentParser(description="Analyze an Apache web log.")
   
    # Creating a new argument to pass in an Apache log file name
    parser.add_argument('-f', '--filename', required=True, type=str, help="Enter an Apache File Name to process")
   
    # Grabbing the argument the user entered
    args = parser.parse_args()
   
    # Create a description to show to the user
    description = "Analyze an Apache web log.  We will look to see if there is anyone trying to hack our website."
    print(description)
   
    # Calling a function to get the summary information of our Apache logfile
    results = IPAddressCount(args.filename)
   
    # Paring out the IP address that is hitting our website the most
    highest_line = results.split('\n')[-2]
    highest_ip = highest_line.split()[1]
    print("IP Address with most hits:", highest_ip)
   
    result = IPLookup(highest_ip)
    ip_info = json.loads(result)
   
    # Print only the information relevant to BitDefender category
    bitdefender_category = ip_info.get('data', {}).get('attributes', {}).get('last_analysis_results', {}).get('BitDefender', {}).get('category')

    if bitdefender_category:
        print("BitDefender Category:", bitdefender_category)
    else:
        print("BitDefender Category not found")
   
    # Open a new file to output our analysis
    with open('apache_analysis.txt', 'w') as apache_log_analysis:
        apache_log_analysis.write(results)

if __name__ == "__main__":
    main()



   