import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     

def deal_card():
    """ Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ take a list of cards and return the score calculated from the cards """
    # blackjack 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # check for all 11 (ace) if the score is already
    # over 21, remove the 11 and replace it with a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """ Compare function between the user and computer"""
    if user_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "Lose, Opponent has BlackJack x)"
    elif user_score == 0:
        return "Win, You have BlackJack x)"
    elif computer_score > 21:
        return "You win :("
    elif user_score > 21:
        return "You Went over. You lose :("
    elif user_score > computer_score:
        return "You Win :D"
    else:
        return "Computer wins :("
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # loop for the user so they can continue taking cards
    while not is_game_over:
        # if the cmpt or user has a blackjack(0) or if the user's score is over 21
        # then end the game 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"     Your cards : {user_cards}, current Score: {user_score}")
        print(f"     Computer's first card : {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, Type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # loop for the computer so the dealer can follow the strategie
    # let thge computer play 
    # should keep it drawing cards as long as it has a score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"     Your Final hand: {user_cards}, Final Score: {user_score}")
    print(f"     Computer's final hand: {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a Game of BlackJack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()