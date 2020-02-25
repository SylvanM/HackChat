import server

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 

import time
  
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
    server.createAccount(username, password)
else:
    while not server.checkAccount(username, password):
        print("Invalid username or password. Please try again.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

host = server.ChatServer(username, password)

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
        messages = host.seeMessagesToMe()
        for i in range(0, len(messages)):
            print(f"""
---> FROM: {messages[i]['from_user']} on {time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(int(messages[i]['timestamp'])))}
{messages[i]['message']}
---> END OF MESSAGE
            """)
    elif action == "3":
        clear()
        messages = host.seeMessageFromMe()
        for i in range(0, len(messages)):
            print(f"""
---> FROM: {messages[i]['to_user']} on {time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(int(messages[i]['timestamp'])))}
{messages[i]['message']}
---> END OF MESSAGE
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
    elif action == "7":
        exit()
    else: 
        clear()
        print("Invalid input, please enter a choice 1-7")


