import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    elif win(user,computer):
        return (f"Congragulations {user} beats {computer}!!!")
    else: 
        return (f"?{computer} beats {user}. Try Again.")  
def win(player, comp):
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or \
        (player == 'p' and comp == 'r'):
        return True

print(play())
