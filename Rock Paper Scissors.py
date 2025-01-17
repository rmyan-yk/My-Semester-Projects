#Rock, Paper, Scissors

#Innit
import random
wins = 0
losses = 0
#Functions
#Main
while True:
#Player's Choice
    print("Welcome to Rock, Paper, Scissors")
    print("Select 1 of the 3 options")
    player = input("Rock, Paper, Scissors...Shoot!!")
#Implement input validation to ensure the player enters a valid move
#(rock, paper, or scissors) and handle any invalid inputs gracefully.
    if player != "rock" or "paper" or "scissors":
        print("please enter a valid response and restart the game :(")
        break
#Computer's Choice
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
        print("Computer chose rock")
    elif computer == 2:
        computer = "paper"
        print("Computer chose paper")
    else:
        computer = "scissors"
        print("Computer chose scissors")

#Determine outcome
#Display the score (e.g., Player: 3 / Computer: 6) after each round, updating it accordingly.
    if player == "rock" and computer == "rock":
        print("Tie")
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "rock" and computer == "paper":
        print("Loss")
        losses = losses + 1
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "rock" and computer == "scissors":
        print("Win")
        wins = wins + 1
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "paper" and computer == "paper":
        print("Tie")
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "paper" and computer == "rock":
        print("Win")
        wins = wins + 1
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "paper" and computer == "scissors":
        print("Loss")
        losses = losses + 1
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "scissors" and computer == "scissors":
        print("Tie")
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "scissors" and computer == "rock":
        print("Loss")
        losses = losses + 1
        print("Player: "+str(wins)+" / Computer: "+str(losses))

    elif player == "scissors" and computer == "paper":
        print("Win")
        wins = wins + 1
        print("Player: "+str(wins)+" / Computer: "+str(losses))

#Ask Player if they want to continue
    playagain = input("Would you like to play again")
    if playagain == "yes":
        print("Restarting...")
    elif playagain == "no":
        print("Bye!")
        break


