import random

def play():
    
    #User vs Computer. Take input from user and use logical comparison cases against the computer. 
    user=input("'r' for Rock,'p' for Paper, 's' for scissors\n")
    computer=random.choice(['r','s','p'])
    
    #If it's a tie
    if user==computer:
        print( "It\'s a tie! Another round?")
        choice=input()
        again(choice)
    #If User wins
    if is_win(user, computer):
        print("You Won! Great! Another round?")
        choice=input()
        again(choice)
    #If user loses. Final case by default, no need for another if/else statement
    print( "You Lost! Another round?")
    choice=input()
    again(choice)

#To prompt user to play again?
def again(user_choice):
    
    if user_choice=='y':
        print(play())
    elif user_choice=='n':
        print("Thank You for Playing!")
        exit()


# GAME RULES: r>p, s>p, p>r
def is_win(player, opponent):
    #return true if player wins (grouped logical conditions)
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(play())

