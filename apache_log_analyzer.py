#!/usr/bin/env python3

# Author:  Rae Denruiter
# Email:  rlanderson1@wisc.edu
# Description:  "Analyze an Apache web log.  We will look to see if there is one trying to hack our website." 

import sys,subprocess,argparse,requests,bs4

#Function to call a website to get more information about an IP address
def IPLookup(ip_address):

    #URL to call to lookup IP
    url = f"https://tools.keycdn.com/geo?host={ip_address}"
    print(url) #Print the URL for verification
    
    #Make a requests to the specified URL
    response = requests.get(url)
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
   
    #Create a description to show to the user
    parser = argparse.ArgumentParser(description="A new parser for our script")  #Intake a file name
    
    #Creating a new argument to pass in an apache log file name (argument=filename, type=string-the default for agrument is string, help=value-value is required at the command line, )
    parser.add_argument('-f', '--filename', required=True,type=str, help="Enter an Apache File Name to process")  #bring in the filename that will be processed
        
    #Grabbing the agrument the user entered (parse arg=function call- allows the help menue to be established, the arg will allow the file from above,)
    args = parser.parse_args()
   
    
    #Create a description to show to the user
    description = "Analyze an Apache web log.  We will look to see if there is anyone trying to hack our website."

    print(description)   


    #Calling a fuction to get the summary information of our apache logfile
    results = IPAddressCount(args.filename)
    
    #Paring out the ip address that is hittin our website the most
    highest_line = results.split('\n')[-2]
    #print(highest_line)
    highest_ip = highest_line.split()[1]
    print(highest_ip)

    result = IPLookup(highest_ip)
    print(result [:250]) ##Print the first 250 characters of the response

    myHTML = bs4.BeautifulSoup(result, features="html.parser") #Pass in only HTML, no other formate

    print(myHTML.find_all("dd", class_="col-8 text-monospace")[1].text) #Chrome, tools, developer tools, click on upper left icon which allows you to select anyhting on the page, click on work and it shows exactly in the HTML script it is

    #Open a new file to output our analysis
    apache_log_analysis = open('apache_analysis.txt', 'w')
    
    apache_log_analysis.write(results)
    #print(results)

    #Closing our analysis file
    apache_log_analysis.close()
    
if __name__ == "__main__":  #Excute the main function-only function being used
    main()


   
