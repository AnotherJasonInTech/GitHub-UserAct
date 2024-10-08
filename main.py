# In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display 
# it in the terminal. This project will help you practice your programming skills, including working with APIs, 
# handling JSON data, and building a simple CLI application.

import urllib.request
import json
from collections import Counter
import os


# Open File - If no File, Create new file with the name passed through

def openFile(jsonFilename):
    try: 
        with open(f"users/"+jsonFilename, 'r') as json_file:
            jsonData = json.load(json_file)
    except: 
        with open("users/"+jsonFilename, 'w') as json_file:
            json_file.write('')
            jsonData = []
    return jsonData

def writeFile(jsonEvents, file):
    entries = []
    for event in jsonEvents:
        entries.append(event)

    with open(filename, 'w') as file:
        json.dump(entries, file, indent=4)


# request the payload, then extract the data from the API request
def extractPayload(url):
    try:
        with urllib.request.urlopen(url) as urlPayload:
            decryptedPayload = urlPayload.read().decode('utf-8')
        # Parse JSON data
        return json.loads(decryptedPayload)
   # Pulled from ChatGPT. Error / Exception Handling
    except urllib.error.HTTPError as e:
        # This block will handle HTTP errors (e.g., 404, 500)
        print(f"HTTP Error: {e.code} - {e.reason}")
        # Added Return 0 so program will quit if error
        return 0

    except urllib.error.URLError as e:
        # This block will handle errors such as no network connection or invalid domain
        print(f"URL Error: {e.reason}")
        # Added Return 0 so program will quit if error
        return 0

    except Exception as e:
        # Handle any other exception that might occur
        print(f"An unexpected error occurred: {str(e)}")
        # Added Return 0 so program will quit if error
        return 0

# This was my first attempt at diplaying the data from the JSON file. Evolved to the second function
# def displayPayload(payload, key):
    
#     eventTypes = []
#     #For Every entry in the payload, pull the type of event
#     for entry in payload:
#         eventTypes.append(entry[key]) 
#     counts = Counter(eventTypes)
#     for item, count in counts.items():
#         print(f"{item} = {count}")
        
# Display The Data pulled form the JSON file
def displayPayload2(payload):
    repos = {}
    
    # Extract the Entry name and request type. Save to a list inside of a dictionary
    for entry in payload:
        entryType = entry["type"]
        entryName = entry["repo"]["name"]

        #if the Repo name does not exist in the dictionary, create it. 
        if entryName not in repos:
            repos[entryName] = []
        # If it exists, add it the the end of the list inside of the dictionary
        else:
            repos[entryName].append(entryType)
    
    # check to see how many repos there are for the user.  
    if len(repos) != 1:
        print(f"- There are {len(repos)} Repos", end="")
    else:
        print(f"- There is {len(repos)} Repo", end = "")
    print(f" in this user's account.")



    repoDictKeys = []
    
    # Look at all of the keys in the dictionary. Keys are the name of the repos. 
    for i in repos.keys():
        repoDictKeys.append(i)
    print()
    counter = 0

    # while the counter is less than the amount if entries in the dictionary/ repos user has:
    while(counter < len(repoDictKeys)):
        # used COUNTER to find/sort the amount of requests
        currentRepo = repoDictKeys[counter]
        event_counts = Counter(repos[currentRepo])
        

        print(f"In the {currentRepo} repo:")
        if len(event_counts.items()) == 0:
            print("There were no events.")
        else: 

            for event, amount in event_counts.items():
                
                
                # Add the space and optional 's' in the request type
                correctedEvent = ""
                for index, char in enumerate(event):
                    if char.isupper() and index != 0:
                        correctedEvent += " " + char
                    else: 
                        correctedEvent += char
                if amount != 0:
                    correctedEvent += "s"
                    print("- There are ", end="")
                else:
                    print("- There is ", end = "")
                print (f"{amount} {correctedEvent}")
        counter += 1
        print()
        




username = input("What is your user name? ")
url = f"https://api.github.com/users/{username}/events"
filename = username + ".json"
print()
print()
print()
payload = extractPayload(url)
if payload == 0:
    quit()
else:
    file = openFile(filename)
    writeFile(payload, file)

displayPayload2(payload)