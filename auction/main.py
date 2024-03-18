from replit import clear

# logo
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
auction = {}
finish = False

# function to find highest bid and its bidder
def winner(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    amount = bidding_record[bidder]
    if amount > highest_bid:
      highest_bid = amount
      winner = bidder
  clear()
  print(
      f"\nThe Winner of this bidding is {winner} with a bid of ${highest_bid}")

# finish or want to add more bidders?
while not finish:
  name = input("What's Your Name: ")
  bid = int(input("What's Your Bid: $"))
  auction[name] = bid
  more = input("Are there any other bidders? yes/no: ")
  if more == "no":
    finish = True
    winner(auction)
  elif more == "yes":
    clear()
