



from random import choice

#
# USER SELECTION
#
valid_choices = ["rock", "paper", "scissors"]

def winner(user_choice, computer_choice):
<<<<<<< Updated upstream
    if user_choice == "rock" and computer_choice == "rock":
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        return "The computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "The user wins"

    elif user_choice == "paper" and computer_choice == "rock":
        return "The user wins"
    elif user_choice == "paper" and computer_choice == "paper":
        return "It's a tie!"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "The computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        return "The computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "The user wins"
    elif user_choice == "scissors" and computer_choice == "scissors":
        return "It's a tie!"
    

# only run this code if we run this script from the command line
# but not if we iomport some code from this file to another file
# prevents execution of code below when we want to test a function in isolation
if __name__ == "__main__":

=======
    return "OOPS - TODO"


if __name__ == "__main__":
>>>>>>> Stashed changes
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

<<<<<<< Updated upstream
    #
    # COMPUTER SELECTION
    #
=======
#
# COMPUTER SELECTION
#
>>>>>>> Stashed changes

    c = choice(valid_choices)
    print("COMPUTER CHOICE:", c)

<<<<<<< Updated upstream
    #
    # DETERMINATION OF WINNER
    #

    # use function from above??
    print(winner(u, c))
=======
#
# DETERMINATION OF WINNER
#

    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")

    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
>>>>>>> Stashed changes
