alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
# welcome
print("***____WELCOME TO THE CAESAR CIPHER____***\n\n")
play_again = True


# a common function for encode and decode
def caesar(massage, shift_amount, direction):
  new_text = ""
  for letter in massage:
    if letter in alphabet:
      position = alphabet.index(letter)

      if direction == "encode":
        new_position = position + shift_amount
      else:
        new_position = position - shift_amount

      new_letter = alphabet[new_position]
      new_text += new_letter
    else:
      new_text += letter

  print(f"\nThe {direction}d text is --> {new_text}")


# call function & initialization

while play_again:
  option = input(
      "\nType 'encode' to encrypt and 'decode' to decrypt: ").lower()
  text = input("\nEnter your massage: ").lower()
  shift = int(input("\nEnter the shift number: "))
  shift = shift % 26
  caesar(text, shift, option)

  play = input("\nDo you Want to go again, type 'yes' or 'no': ").lower()
  if play == "yes":
    play_again = False
    print("\nGood-Bye :)")
