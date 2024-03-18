# higher lower
from replit import clear
import random 
from game_data import data
from art import logo,vs
# Actual code
 

#----------------------------------Functions----------------------------------

def formate(account):
  """formating the information stored in dictionary in data list"""
  account_name = account["name"]
  account_info = account["description"]
  account_country = account["country"]
  return  f"{account_name}, a {account_info} From {account_country}"
  

def compare(guess,accA,accB):
  """Comaparing the followers of A and B and comparing guess with answer"""
  answer = "a" if accA>accB else "b"
  return guess == answer


#----------------------------------Content code----------------------------------
score = 0
should_continue  = True
accountB = random.choice(data)
print(logo)
print("\n\tWe are Comparing two celebreties, ")
print("\tYou Have to tell Who has More Followers on Instagram\n")


while should_continue:
  #assigning Accounts to veriables and calling functions
  accountA = accountB
  accountB = random.choice(data)
  while accountA == accountB:
    accountB = random.choice(data)
    
  # printing statements
  
  print(f"\n\tCompare A: {formate(accountA)}")
  print(vs)  
  print(f"\tAgainst B: {formate(accountB)}")
  
  #get a guess from user
  guess = input("\n\tWho Has More Followers, 'A' or 'B': ").lower()
  
  # getting Followers of A and B
  followerA =  accountA["follower_count"]
  followerB =  accountB["follower_count"]
 
  # Comaparing the followers of A and B
  is_correct = compare(guess,followerA,followerB)

  clear()
  print(logo)
  # feedback to user on their answer
  if is_correct:
    score+=1
    print(f"\n\tYou're Right!, Current Score: {score}") 
  else:
    should_continue = False
    print(f"\n\tSorry, That's wrong!, Your Final score is {score}")
  