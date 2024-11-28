import random 
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def play_round():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    while user_choice not in choices:
        print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    computer_choice = random.choice(choices)
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    while True:
        result = play_round()
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"\nScore: You: {user_score} | Computer: {computer_score}")
        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break
if __name__ == "__main__":
    main()
