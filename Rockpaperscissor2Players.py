player1 = input("Player 1, Enter your input: ")
print("You cannot see the input of player 1 \n \n" * 20)

player2 = input("Player 2,Enter your input ")

if player1 == 'rock' and player2 == 'paper':
	print("Player 2 wins")
elif player1 == 'paper' and player2 == 'scissor':
	print("Player 2 wins")
elif player1 == 'scissor' and player2 == 'rock':
	print("Player 2 wins")
elif player1 == player2:
	print("It's a tie")
else:
	print("Player 1 wins")