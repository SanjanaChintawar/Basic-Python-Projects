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
import random
from replit import clear

# Function for creating a random card from cards list
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Sum function for adding the cards
def calculate_score(cards):
  """Gives sum of the card faces"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # if cards sum is above 21 or equals to 21
  if 11 in cards and sum(cards) < 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


# compare function returns highest score or who wins
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "\nYou went over. You lose 😤"

  if user_score == computer_score:
    return "\nDraw 🙃"
  elif user_score == 0:
    return "\nYou Win with a Blackjack 😎"
  elif computer_score == 0:
    return "\nLose, Opponent has Blackjack 🙁"
  elif user_score > 21:
    return "\nYou went over, Lose 😒"
  elif computer_score > 21:
    return "\nOpponent Went over, You Win 🤗"
  elif user_score > computer_score:
    return "\nUser win 😁"
  else:
    return "\nOppoenet scored highest, You lose 🥲"


def play_game():

  print(logo)

  #Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #loop for initial stage

  while not is_game_over:
    #call score function
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\n   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #pass or not
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Computer's strategy
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\n   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#want to play again?
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()