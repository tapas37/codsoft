import random
def take_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice!")
def take_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def okay():
    user_score = 0
    computer_score = 0
    while True:
        print("\n===== Rock, Paper, Scissors Game =====")
        user_choice = take_user_choice()
        computer_choice = take_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        print(f"\nScores - You: {user_score} | Computer: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':

            if user_score>computer_score:
                print("Thanks for playing! you won")
            else:
                print("thanks for playing")
            break
okay()