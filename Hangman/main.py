import clear
print("Welcome To Hangman Word Guessing Game\n")
print("You have 6 lives to guess the word\n.......All the Best.......\n\n")

import random
# hangman drawing
stages = [
    '''
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
'''
]
# random word

import words

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

disply = []
for letter in range(word_length):
  disply += "_"
print(f"{' '.join(disply)}")

# choose the letter
turn = 0
lives = 6
end = False

# loop for guessing the letter
while not end:

  guess = input("\n\nEnter the letter : ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if (letter == guess):
      disply[position] = letter

  print(f"\n{' '.join(disply)}")

  # lose
  if guess not in chosen_word:
    print(
        f"\nyou gussed a letter '{guess}' which is not in the word...You lose a life :("
    )
    lives -= 1
    if lives == 0:
      end = True
      print("\nYou Lose..!\n")
      print(f'The word is {chosen_word}')

# win
  if "_" not in disply:
    end = True
    print("\n\nYou Win...!\n")
    print(f'Yeah! The word is {chosen_word}')

  # print hangman
  print(stages[lives])

  # divider
  turn += 1
  if lives == 0:
    print(f'\n-----------------------GAME OVER----------------------\n')
  elif "_" not in disply:
    print(f'\n-----------------------GAME OVER----------------------\n')
  else:
    print(f'\n-----------------------{turn}----------------------\n')
clear()