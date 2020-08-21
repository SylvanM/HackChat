# HackChat
A very easily hackable chat service I designed for the Cybersecurity club at my school.

Chances are, by the time you're reading this, our free trial for the web hosting service will be over and this will no longer work.
If for some reason you really want to see this in action, the code for the API can be found [here](https://github.com/SylvanM/chat-service). Somehow get the code
running on some web hosting service and change the url in ```server.py``` at the top of the file.

## Overview
This is a python chat app that uses the API I made, [here](https://github.com/SylvanM/chat-service). It's a console based application that lets users send messages to each other.
Please note that this app is **deliberately insecure.** It is designed to illustrate SQL injection and a man-in-the-middle attack, since anyone with an administrator account can intercept messages.

### Usage
Run the ```chat-app.py``` program. You will be greeted with the following screen:

```
Welcome to our crappy chat service we made to be purposely hackable. 
Please select one of the following uptions

    1. Create Account
    2. Login to an existing account
    3. Automate Administrator

Enter the number of the choice you want: 
```

As you can see, we didn't have a great UI budget. 

Choosing option 3, "Automate Administrator," will set up a loop that will constantly allow every sent message to be delivered instead of it waiting to be approved manually by an admin.

Once you've logged in or created an account, you'll be given a list of actions.

```
Choose an action:

    1. Send a message
    2. See messages to you
    3. See messages from you
    4. See pending messages (ADMIN ONLY)
    5. Accept a message (ADMIN ONLY)
    6. Block a message (ADMIN ONLY)
    7. Exit
    
Enter the number of the action you want to do: 
```

### Administrator actions

As said before, this app was also meant to demonstrate the man-in-the-middle attack, as well as other methods for communciating over an insecure network.
Having administrators, which can block or approve messages, tamper messages, or send a message mascerading as another user, is our best way of replicating that.
