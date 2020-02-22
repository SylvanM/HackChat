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
        return json.loads(results)

    def seeMessageFromMe(self):
        params = {
            "f": "getf",
            "user"  : self.username,
            "pass"  : self.password
        }

        results = requests.get(url = url, params = params)
        return json.loads(results)

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
        print(results.text)

    def blockMessage(self, message_id):
        if not self.isAdmin():
            return False

        params = {
            "f": "blckmsg",
            "adusr": self.username,
            "adpss": self.password,
            "mid" : message_id
        }

        result = requests.post(url = url, params = params)
        print(result.url)
    
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

