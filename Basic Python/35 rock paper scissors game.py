import random #import this module for random choices in the game.

while True:
    choices = ["rock","paper","scissors"] #make the choices for the random outcome.

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower() #lower allows omits case sensitive inputs.
        if player == computer:
            print ("computer: ",computer)
            print ("player: ", player)
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
        elif player == "scissors":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
        elif player == "paper":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye.")