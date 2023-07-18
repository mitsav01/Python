import random
computer = random.randint(0,2);
player1 = input("Player 1, Enter your input: ").lower


if computer == 0:
	computer = "rock"
elif computer == 1:
	computer = "paper"
else:
	computer = "scissor"
print(f"Computer = {computer}")
if player1 == 'rock' and computer == 'paper':
	print("Computer wins")
elif player1 == 'paper' and computer == 'scissor':
	print("Computer wins")
elif player1 == 'scissor' and computer == 'rock':
	print("Computer wins")
elif player1 == computer:
	print("It's a tie")
else:
	print("Player 1 wins")