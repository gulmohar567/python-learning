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
            return "You win!"
        else:
            return "Computer wins!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid input!"
    
outcome = get_winner(get_choices()) 
print(outcome)



