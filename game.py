import random

def computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action

def user_choice():
    user_action = input("Enter a choice (rock, paper, scissors): ")
    return user_action

def result(user_action,computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

if __name__ == '__main__':
    
        computer_action=computer_choice()
        user_action=user_choice()
        result(user_action,computer_action)

        play_again = input("Play again? (y/n): ")
        