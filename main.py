# In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display 
# it in the terminal. This project will help you practice your programming skills, including working with APIs, 
# handling JSON data, and building a simple CLI application.

import urllib.request
import json
from collections import Counter
import os

def openFile(jsonFilename):
    try: 
        with open(jsonFilename, 'r') as json_file:
            jsonData = json.load(json_file)
    except: 
        with open(jsonFilename, 'w') as json_file:
            json_file.write('')
            jsonData = []
    return jsonData

def extractPayload(url):
    try:
        with urllib.request.urlopen(url) as urlPayload:
            decryptedPayload = urlPayload.read().decode('utf-8')
        # Parse JSON data
        return json.loads(decryptedPayload)
    except: 
        print("Error Connecting to GitHub, Please check connection and username.")
        return 0

def writeFile(jsonEvents, file):
    entries = []
    for event in jsonEvents:
    # print(f"Repository Name: {repo['name']}, URL: {repo['html_url']}")
        entries.append(event)

    with open(filename, 'w') as file:
        json.dump(entries, file, indent=4)

def displayPayload(payload, key):
    eventTypes = []
    for entry in payload:
        eventTypes.append(entry[key]) 
    counts = Counter(eventTypes)
    for item, count in counts.items():
        print(f"{item} = {count}")
        

def displayPayload2(payload, key):
    repos = {}
    for entry in payload:
        # if entry["repo"]["name"] in repos:
        repos[entry["repo"]["name"]] = [] 
            #if entry["type"] in repos[entry["repo"]["name"]]:
            #    repos["name"][entry["type"]] += 1
            #else:
            #    repos["name"][entry["type"]] = 1
        # else:
        #     repos[entry["repo"]["name"]] = []
        #     #if entry["type"] in repos[entry["repo"]["name"]]:
        #     #    repos["name"][entry["type"]] += 1 
        #     #else:
        #     #    repos["name"][entry["type"]] = 1

    for key, value in repos.items(): 
        print (key, ":", value)

# Replace 'username' with the GitHub username you want to look up
username = input("What is your user name? ")
url = f"https://api.github.com/users/{username}/events"
filename = username + ".json"
# Make a GET request to the GitHub API


payload = extractPayload(url)
if payload == 0:
    quit()
else:
    file = openFile(filename)
    writeFile(payload, file)

displayPayload2(payload, "type")