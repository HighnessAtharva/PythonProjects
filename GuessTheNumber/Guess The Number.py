import random
def guess(x):
    random_number=random.randint(1, x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess< random_number:
            print("Sorry, guess again, too low")
        elif guess>random_number:
            print("Sorry, guess again, too high")
    print(f"Yay, congrats, you have guessed the number {random_number} correctly.")    

#Uncomment this to call the function 
'''guess(10)'''  #Argument x is the range from 1 to x

def computer_guess(x):
    low, high= 1, x
    feedback=''
    while feedback!='c':
        if low!=high:  #C being correctly guessed
            guess=random.randint(low, high)
        else:
            guess=low #Could also be high b/c low=high as computer narrows it down. Upper bound and lower bound become same.
        feedback=input(f"Is {guess} too high (H), too low (L) or correct(C)?").lower() #converting input to lowercase
        if feedback == 'h':
            high = guess-1 
        elif feedback == 'l':
            low = guess+1   

    print(f"Yay, the computer guessed the number {guess} correctly!")    

computer_guess(10000)  #Argument x is the range from 1 to x