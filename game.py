import random

def get_user_choice():
    #Function to prompt the user to choose rock, paper, or scissors.
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    #Function to randomly select rock, paper, or scissors for the computer.
    
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    
    #Function to compare user's choice with computer's choice and determine the winner.
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


while True:
# Get user choice
    user_choice = get_user_choice()

    # Get computer choice
    computer_choice = get_computer_choice()
    print(f"Computer chooses {computer_choice}.")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

