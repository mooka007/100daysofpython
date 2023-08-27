import random

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

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


# if the cmpt or user has a blackjack(0) or if the user's score is over 21
# then end the game 
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards : {user_cards}, current Score: {user_score}")
print(f"Computer's first card : {computer_cards[0]}")


if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True