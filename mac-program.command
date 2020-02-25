#!/usr/bin/env python

import requests
import json.decoder

url = "https://rhscybersecurity.000webhostapp.com/chat.php"


def createAccount(username, password):
    params = { 
        "f" : "cusr",
        "user" : username,
        "pass" : username
    }

    requests.get(url = url, params = params)


def checkAccount(username, password):
    params = { 
        "f" : "v",
        "user" : username,
        "pass" : username
    }

    result = requests.get(url = url, params = params).text
    return result

class ChatServer:

    def __init__(self, usr, pwd):
        self.username = usr
        self.password = pwd

    # returns whether or not the user is an administrator
    def isAdmin(self):
        params = {
            "f": "a",
            "adusr": self.username,
            "adpss": self.password
        }

        result = requests.get(url = url, params = params)
        return result

    # delete my account
    def deleteAccount(self):
        params = {
            "f": "dusr",
            "user" : self.username,
            "pass" : self.password
        }

        requests.get(url = url, params = params)

    # send a message to another user
    def sendMessage(self, to_user, message):
        params = {
            "f": "sndmsg",
            "user"  : self.username,
            "pass"  : self.password,
            "msg"   : message,
            "to"    : to_user
        }

        result = requests.get(url = url, params = params)

    def seeMessagesToMe(self):
        params = {
            "f": "rfsh",
            "user"  : self.username,
            "pass"  : self.password
        }

        results = requests.get(url = url, params = params)
        print(results.url)
        return json.loads(results.json())

    def seeMessageFromMe(self):
        params = {
            "f": "getf",
            "user"  : self.username,
            "pass"  : self.password
        }

        results = requests.get(url = url, params = params).json()
        return json.loads(results)

    # admin functions

    def acceptMessage(self, message_id):
        if not self.isAdmin():
            return False

        params = {
            "f": "",
            "adusr": self.username,
            "adpss": self.password,
            "mid" : message_id
        }

        results = requests.get(url = url, params = params)

    def blockMessage(self, message_id):
        if not self.isAdmin():
            return False

        params = {
            "f": "blckmsg",
            "adusr": self.username,
            "adpss": self.password,
            "mid" : message_id
        }
    
    def seePending(self):
        if not self.isAdmin():
            return False
        
        params = {
            "f": "seepndg",
            "adusr": self.username,
            "adpss": self.password
        }

        results = requests.get(url = url, params = params).json()
        return json.loads(results)


# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

validInput = False

choice = "0"

print("""
Welcome to our crappy chat service we made to be purposely hackable. 
Please select one of the following uptions

    1. Create Account
    2. Login to an existing account
    3. Automate Administrator
""")

while not validInput:
    choice = input("Enter the number of the choice you want: ")

    if (choice == "1" or choice == "2" or choice == "3"):
        validInput = True
    else:
        print("Please enter a valid choice.")

username = input("Enter your username: ")
password = input("Enter your password: ")

    
if choice == "1":
    createAccount(username, password)
else:
    while not checkAccount(username, password):
        print("Invalid username or password. Please try again.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

host = ChatServer(username, password)

if choice == "3":
    while True:
        pending = host.seePending()
        clear()
        print("Pending Messages:")
        print(pending)

        for message in pending:
            host.acceptMessage(message["message_id"])

        sleep(.5)

clear()

while True:
    print("""
Choose an action:

    1. Send a message
    2. See messages to you
    3. See messages from you
    4. See pending messages (ADMIN ONLY)
    5. Accept a message (ADMIN ONLY)
    6. Block a message (ADMIN ONLY)
    7. Exit
    """)

    action = input("Enter the number of the action you want to do: ")
    
    if action == "1":
        clear()
        host.sendMessage(input("TO: "), input("MESSAGE: "))
    elif action == "2":
        messages = host.seeMessageFromMe()
        for i in range(0, len(messages)):
            print(f"""
----------------------------------------------
FROM: {messages[i]['from_user']}

{messages[i]['message']}
            """)
    elif action == "3":
        clear()
        messages = host.seeMessageFromMe()
        for i in range(0, len(messages)):
            print(f"""
----------------------------------------------
TO: {messages[i]['to_user']}

{messages[i]['message']}
            """)
    elif action == "4":
        if not host.isAdmin():
            clear()
            print("You are not an administrator!")
            continue

        print(host.seePending())
    elif action == "5":
        if not host.isAdmin():
            clear()
            print("You are not an administrator!")
            continue
        host.acceptMessage(input("Enter message ID: "))
    elif action == "6":
        if not host.isAdmin():
            clear()
            print("You are not an administrator!")
            continue
        host.blockMessage(input("Enter message ID: "))
    else:
        exit()



