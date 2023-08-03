import random

word_list  = ["hmidalamba", "9assamBoT9achar","statia"]
chosen_word = random.choice(word_list).lower()

display = []
for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
