
print("----Welcome to Rock Paper Scissor Game----")
 
print("0 = Rock:") 
print("1 = Paper:") 
print("2 = Scissor:") 

# import random module
import random

def get_user_choice():
    user_choice = int(input("Choose 0 for rock, 1 for paper, 2 for scissors: "))
    return user_choice

def get_computer_choice():
    choices = [0, 1, 2]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
#0==0, 1==1, 2==2        
        return "Opps it's a tie!"
    elif (user_choice == 0 and computer_choice == 2)or(user_choice == 2 and computer_choice == 1)or(user_choice == 1 and computer_choice == 0):
# rock beats scissor, scissor beats paper, paper beats rock       
        return " Hurrah,You win!"
    else:
        return "Computer wins! Better luck next time"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print("----Thanks for playing-----")

play_game()
