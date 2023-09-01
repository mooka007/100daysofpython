import random
import os
logo = """   
        ,-.-.  ,-,--.  
 ,--.-./=/ ,/,-.'-  _\ 
/==/, ||=| -/==/_ ,_.' 
\==\,  \ / ,\==\  \    
 \==\ - ' - /\==\ -\   
  \==\ ,   | _\==\ ,\  
  |==| -  ,//==/\/ _ | 
  \==\  _ / \==\ - , / 
   `--`--'   `--`---'  
            
"""
data = [
    {
        'name' : 'Instagram',
        'follower_count' : 346,
        'description' : 'Social media Platform',
        'country' : 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count' : 215,
        'description' : 'Footballer',
        'country' : 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count' : 183,
        'description' : 'Musician & Actress',
        'country' : 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count' : 181,
        'description' : 'Actor and Professional Wrestler',
        'country' : 'Uinted States'
    },
    {
        'name': 'Neymar',
        'follower_count' : 138,
        'description' : 'Footballer',
        'country' : 'Brazil'
    },
    {
        'name': 'National Geographic',
        'follower_count' : 135,
        'description' : 'Magazine',
        'country' : 'Emirates'
    },
    {
        'name': 'Oum Keltoum',
        'follower_count' : 456,
        'description' : 'Musician',
        'country' : 'Egypt'
    },
    {
        'name': 'Stati',
        'follower_count' : 76,
        'description' : 'Musician ',
        'country' : 'Morocco'
    },
    {
        'name': 'Saad Lamjared',
        'follower_count' : 786,
        'description' : 'Musician',
        'country' : 'Morocco'
    },
    {
        'name': 'Mahmoud Darwich',
        'follower_count' : 689,
        'description' : 'Poet',
        'country' : 'Palestine'
    }
]


def data_format(account):
    """ make it in one form and apply it on 2 account a & b
        and returns printable format
    """
    account_name = account["name"]
    account_description = account["description"]
    accout_country = account["country"]
    return (f"{account_name}, a {account_description}, from {accout_country}")

def check_answer(guess, a_followers, b_followers):
    """ checking the user is correct or not 
            Guess A | Guess B
    a > b |    v    |    x
    B > A |    x    |    v
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
repeat = True
account_b = random.choice(data)

while repeat:
    # making account at position b become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare a : {data_format(account_a)}")
    print(logo)
    print(f"Against B : {data_format(account_b)}")


    guess = input("Who has more Followers? Type 'A' or 'B' : ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the console once your answer is right
    os.system('cls')

    # giving a feedback on their guess
    if is_correct:
        score += 1
        print(f"You're Right ! Hell Ya \m/, Current Score : {score}")
    else:
        repeat = False
        print(f"Sorry Wrong Answer ( . )( . ), Your Final Score is {score}")