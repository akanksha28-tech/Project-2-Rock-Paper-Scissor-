import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("=== Rock-Paper-Scissors Game ===")
    user = get_user_choice()
    computer = get_computer_choice()

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    result = determine_winner(user, computer)
    print(f"\nResult: {result}")

    again = input("\nPlay again? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
play_game()

