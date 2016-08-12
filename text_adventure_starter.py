start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
	print("You decide to go left and you see that there are two doors: one door is red and one door is green. What door do you choose?")
	print("Type 'green' to go through the green door or 'red' to go through the red door")
	user_input = input()
	if user_input == "green":
		print ("Congrats, you are safe!")
	elif user_input == "red":
		print("Sorry, you fell through the Earth and died!")
	#while user_input != "red" or "green":
		#user_input == input("Enter red or green ")
elif user_input == "right":
	print("You choose to go right and you come across a shoreline. You can decide whether you want to swim or take the boat that is next to the shoreline. What do you choose?") # finished the story writing what happens
	print ("Type 'swim' to swim across or type 'boat' to take the boat across.")
	user_input = input()
	if user_input == "swim":
		print("Wow, you are an amazing swimmer, and you survived!")
	elif user_input == "boat":
		print("I'm sorry, the boat had a hole and you drowned!")
	
	#while user_input != "swim" or "boat":
		#user_input == input("Enter swim or boat ")
#while user_input != "right" or "left":
	#user_input == input("Enter right or left ")   #these aren't supposed to work
	


