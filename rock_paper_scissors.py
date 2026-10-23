import random

def player_choice():
    choice = input("Enter your choice (r,p,c): ")
    if choice not in ['r', 'p', 'c']:
        print("Invalid choice. Please enter r, p, or c.")
        return player_choice()
    return choice

def computer_choice():
    return random.choice(['r', 'p', 'c'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "r" and computer == "c") or (player == "p" and computer == "r") or (player == "c" and computer == "p"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        player = player_choice()
        computer = computer_choice()
        print(f"You chose {player}")
        print(f"Computer chose {computer}")
        print(determine_winner(player, computer))

if __name__ == "__main__":
    main()