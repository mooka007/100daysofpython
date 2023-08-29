from random import randint
import os 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Nice Shot!")
    

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome  to the Guessing Game! ")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(answer)


    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number. ")

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if guess != answer:
            print(f"You still have {turns} attempts")
        if turns == 0:
            print("You've run out of guesses, You Lose")
            return            
game()