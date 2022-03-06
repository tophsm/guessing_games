#Guessing game with roles reversed. User will try to guess a random number chosen by computer.
import random

def guess(x):
    random_num = random.randint(1, x) #randint will select random int between (a,b) inclusive
    guess = 0 #starting point. Guess will never actually be 0.
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: ")) 

        if guess < random_num:
            print("Sorry, your guess was too low. Try again.")
        elif guess > random_num:
            print("Sorry, your guess was too high. Try again.")
    print(f"Yayy! You got it! {random_num} was the correct number.") #prints when guess == random_num


guess(10) #sets x = 10