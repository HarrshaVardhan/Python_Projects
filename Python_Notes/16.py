#command = ""
#while command.lower() != "quit":
#	command = input("> ")
#	if command.lower() == "start":
#		print("Car started...")
#	elif command.lower() == "stop":
#		print("Car stopped.")


#improved code one

#command = ""
#while command != "quit":
#	command = input("> ").lower()
#	if command == "start":
#		print("Car started...")
#	elif command == "stop":
#		print("Car stopped.")
#	elif command == "help":
#		print('''
#start - to start the car
#stop - to stop the car
#quit - to quit 
#		''')
#	else:
#		print("Sorry, I don't understand that")


#improve code two

command = ""
while True:
	command = input("> ").lower()
	if command == "start":
		print("Car started...")
	elif command == "stop":
		print("Car stopped.")
	elif command == "help":
		print('''
start - to start the car
stop - to stop the car
quit - to quit 
		''')
	elif command == "quit":
		break
	else:
		print("Sorry, I don't understand that")
