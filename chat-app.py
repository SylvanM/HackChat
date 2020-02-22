import server

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

while True:
    print("""
Choose an action:

    1. Send a message
    2. See messages to you
    3. See messages from you
    4. See pending messages (ADMIN ONLY)
    5. Accept a message
    6. Block a message""")

    action = input("Enter the number of the action you want to do: ")
    
    if action == "1":
        host.sendMessage(input("TO: "), input("MESSAGE: "))
    elif action == "2":
        print(host.seeMessagesToMe())
    elif action == "3":
        print(host.seeMessageFromMe())
    elif action == "4":
        print(host.seePending())
    elif action == "5":
        host.acceptMessage(input("Enter message ID: "))
    elif action == "6":
        host.blockMessage(input("Enter message ID: "))


