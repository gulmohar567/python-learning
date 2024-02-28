import random
def get_choices():
    player_choice = input ("Enter your choice: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    return choices

def get_winner(choices):
    player = choices["player"]
    computer = choices["computer"]
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors!You win!"
        else:
            return "Paper covers rock!Computer wins!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock!You win!"
        else:
            return "Scissors cuts paper!Computer wins!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper!You win!"
        else:
            return "Rock smashes scissors!Computer wins!"
    else:
        return "Invalid input!"
    
outcome = get_winner(get_choices()) 
print(outcome)



