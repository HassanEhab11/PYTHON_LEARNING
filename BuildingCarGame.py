'''

user_help = input("> ")
print("start - to start the car")
print("stop - to stop the car")
print("quit - to exit")

if user_help.upper() == "HELP":
    user_input = input("> ")
    while user_input.upper() != "QUIT":
        if user_input.upper() == "START":
            print("car started ... ready to go !")
        elif user_input.upper() == "STOP":
            print("car stopped ...  !")
        else:
            print("I dont understand that ...")
        user_input = input()
'''
command =""   # i can remove this and the code work effectly
started = False
stoped = False
started = False
while True:
    command = input("> ").upper()
    if command == "START":
        if started:
            print("Car is already started")
        else:
            print("car started ... ready to go !")
            started = True
    elif command == "STOP":
        if not started:
            print("Car is already stopped")
        else:
            print("car stopped ...  !")
            started = False
    elif command == "HELP":
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "QUIT":
        break
    else:
        print("I dont understand that ...")
