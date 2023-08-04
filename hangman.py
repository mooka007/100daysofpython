import random

words = ["btata", "maticha", "gar3a", "falfla"]
chosen_word = random.choice(words).lower()

# blank list to check if its the right letter or not
display = []
for letter in range(len(chosen_word)):
    display += "-"

# loop to check if everything is right or not
theEnd = False
while not theEnd:
    guess = input("Guess the letters: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "-" not in display:
        theEnd = True
        print("You win! Congratulation :)")
    
