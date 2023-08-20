logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidRecord):
  highBid = 0
  winner = ""
  # bidRecord = {"Angela": 123, "James": 321}
  for bidder in bidRecord:
    amount = bidRecord[bidder]
    if amount > highBid: 
      highBid = amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highBid}")
  

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('cls')
  
