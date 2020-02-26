import requests
import json.decoder

url = "https://rhscybersecuritybackup.000webhostapp.com/chat.php"


def createAccount(username, password):
    params = { 
        "f" : "cusr",
        "user" : username,
        "pass" : password
    }

    
    response = requests.get(url = url, params = params)
    print(response.url)


def checkAccount(username, password):
    params = { 
        "f" : "v",
        "user" : username,
        "pass" : password
    }

    result = requests.get(url = url, params = params)
    print(result.url)
    print(result.text)
    return result.text == "true"

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
        print(result.url)
        return result.json()

    # delete my account
    def deleteAccount(self):
        params = {
            "f": "dusr",
            "user" : self.username,
            "pass" : self.password
        }

        response = requests.get(url = url, params = params)

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
        print(result.url)

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

        results = requests.get(url = url, params = params)
        print(results.url)
        return json.loads(results.json())

    # admin functions

    def acceptMessage(self, message_id):
        if not self.isAdmin():
            return False

        params = {
            "f": "acptmsg",
            "adusr": self.username,
            "adpss": self.password,
            "mid" : message_id
        }

        results = requests.get(url = url, params = params)
        print(results.url)

    def blockMessage(self, message_id):
        if not self.isAdmin():
            return False

        params = {
            "f": "blckmsg",
            "adusr": self.username,
            "adpss": self.password,
            "mid" : message_id
        }

        response = requests.get(url = url, params = params)
        print(response.url)
    
    def seePending(self):
        if not self.isAdmin():
            return False
        
        params = {
            "f": "seepndg",
            "adusr": self.username,
            "adpss": self.password
        }

        results = requests.get(url = url, params = params)
        print(results.url)
        return json.loads(results.json())

