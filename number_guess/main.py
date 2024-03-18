logo = """\t\t
                   _____                       _ _     _ 
                  |  __ \                     (_| |   | |
                  | |  \/_   _ ___  ___  ___   _| |_  | |
                  | | __| | | / __|/ _ \/ _ \ | | __| | |
                  | |_\ | |_| \__ |  __|  __/ | | |_  |_|
                   \____/\__,_|___/\___|\___| |_|\__| (_)
                                                         
                                                         
"""
from random import randint

print(logo)

def levels():
  # level = easy or hard
  level = input("\n\tChoose the difficulty. Type 'easy' Or 'hard'👉 ").lower()
  if level == "easy":
    turns = EASY_MOVES
  else:
    turns = HARD_MOVES
  return turns

# Check the answer
def check_ans(guess, answer):
  if guess > answer:
    print("\tToo High🤯")
  elif guess < answer:
    print("\tToo Low😲")
  elif guess == answer:
    print(f"\n\tYes You Are Right It's {answer}\n")


# constant moves
EASY_MOVES = 10
HARD_MOVES = 5

def game():
  # welcome
  print("\t🎲_🎲_🎲_🎲_🎲_Welcome to The Number Guessing Game_🎲_🎲_🎲_🎲_🎲\n")
  print(
      "\n\tI'm Thinking of a Number Between 1 and 100 🤔 \n\t\tCan You guess It ?🧐")
  
  # random number
  answer = randint(1, 100)

  # number of attempts
  turns = levels()
  print(f"\n\tYou have {turns} attempts to guess the number.")

  # repeat this to ask user for guess until it matches to the answer
  guess = 0
  while guess != answer and turns != 0:
    turns -= 1
    guess = int(input("\n\tGuess the Number 👉 "))
    check_ans(guess, answer)
    print(f"\tYou have {turns} remaining Number of attempts.")

  # prints the lost or win statement
  if turns == 0:
    print(f"\n\tNo remaining Attempts..! You lost😭, The Number is {answer}")
  else:
    print("\n\n\tYeah You Win...👑")


game()
