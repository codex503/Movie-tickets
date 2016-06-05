#a simple program to let a user know ticket prices based on age.
prompt = "What is your age?"
active = True

while active:
	age = int(input(prompt))

	if int(age) < 3:
		print ("The ticket is free!")

	

	if int(age) >= 3 and age <= 12:
		print ("The ticket cost $10")
		

	if int(age) > 12:
		print ("The ticket costs $15")
	
		
		
	question = input("\nDo you want to try again? y/n ")
	
	
	if question == 'n':
		active = False

