#A guessing game. User picks a random number and the computer tries to guess correctly.
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?")

        if feedback == 'H':
            high = guess - 1 #when guess is too high, the limit is lowered by at least 1
        elif feedback == 'L':
            low = guess + 1 #limit is increased by at least 1
    print(f"Congrats computer! You guessed {guess} correctly!")

computer_guess(10) #don't forget to include this! This will set your x.