import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["btata", "maticha", "gar3a", "falfla"]
chosen_word = random.choice(words).lower()
lives = 6
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

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            theEnd = True
            print('Game Over')

    print(f"{' '.join(display)}")


    if "-" not in display:
        theEnd = True
        print(" Congratulation! You win :)")
    
    print(stages[lives])
# ghadi nzid whd function kat randomi words by inputf