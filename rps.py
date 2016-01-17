from random import randint

# Global variables for the player's record
playerLoss = 0
playerWin = 0
draw = 0

while 1:

	# Generate computer's choice of RPS
	compChoiceNum = randint(1,3)
	if compChoiceNum == 1:
		compChoice = "Rock"
	if compChoiceNum == 2:
		compChoice = "Paper"		
	if compChoiceNum == 3:
		compChoice = "Scissors"

	# Ask user for choice
	choice = input("Rock, Paper or Scissors? ")

	if choice == "Rock":
		choiceNum = 1
	elif choice == "Paper":
		choiceNum = 2
	elif choice == "Scissors":
		choiceNum = 3
	else:
		print("Sorry, that's not an option!")
		continue

	# Compare users choice against computer's choice
	if choiceNum-compChoiceNum == 0:
		print("Computer chose {0} and you chose {1}. It's a draw".format(compChoice, choice))
		draw += 1
		print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))
	elif choiceNum+compChoiceNum == 4:
		if choiceNum == 1:
			print("Computer chose {0} and you chose {1}. You win!".format(compChoice, choice))
			playerWin += 1
			print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))
		else:
			print("Computer chose {0} and you chose {1}. You lose :(".format(compChoice, choice))
			playerLoss += 1
			print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))
	elif choiceNum+compChoiceNum == 5:
		if choiceNum == 3:
			print("Computer chose {0} and you chose {1}. You win!".format(compChoice, choice))
			playerWin += 1
			print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))
		else:
			print("Computer chose {0} and you chose {1}. You lose :(".format(compChoice, choice))
			playerLoss += 1
			print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))
	elif choiceNum+compChoiceNum == 3:
		if choiceNum == 2:
			print("Computer chose {0} and you chose {1}. You win!".format(compChoice, choice))
			playerWin += 1
			print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))
		else:
			print("Computer chose {0} and you chose {1}. You lose :(".format(compChoice, choice))
			playerLoss += 1
			print("Score: {0} wins, {1} losses, {2} draws.".format(playerWin, playerLoss, draw))

	# Ask user to replay
	again = input("Keep playing? (y/n): ")
	if again == "y":
		continue
	elif again == "n":
		break
	else:
		print("I'm forcing you to play again... Next time type y or n")
		continue