

#improve code no need to repeat .lower every command.

command = ""
while True:
    command = input("> ").lower
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - stop the car
quit - to quit
        """)
    elif command == "quite":
        break
    else:
        print("Sorry, I don't understand that.")
