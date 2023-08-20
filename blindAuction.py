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


print(logo)

bids = {}

bidding_finished = False

while not bidding_finished:
    name = input("what is your name ? ")
    price = input("what is your price ? ")
    bids[name] = price
    input("are there any other bidders ? Type Yes or No ")
    continuee = input("are there any other bidders ? Type Yes or No ")
    if continuee == "No":
        bidding_finished = True