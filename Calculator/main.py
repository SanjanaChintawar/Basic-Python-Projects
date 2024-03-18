#calculator logo
from replit import clear
logo = """
 _____________________
|  _________________  |
| | Calculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#functions for operations
def addition(num1,num2):
  return num1 + num2
  
def subtract(num1,num2):
  return num1 - num2

def product(num1,num2):
  return num1 * num2
  
def divide(num1,num2):
  return num1 / num2

#calculaor main function
def calculator():
  print(logo)
  num1=float(input("\nEnter the First number: "))
  operations={
    "+":addition,
    "-":subtract,
    "*":product,
    "/":divide,
  }
  
  for keys in operations:
    print(keys)
  
  cal_again=True

  #loop for operations on previous answer 
  while cal_again:
    operator=input("\npick an operator: ")
    num2=float(input("\nWhat's the next number: "))    
    calculations=operations[operator]
    result=calculations(num1,num2)    
    print(f"\n{num1} {operator} {num2} = {result}")    
    start=input(f"\ndo you want more operation with {result} or want to start again: ? y/n/again ")
    if start=="y" : 
      num1=result
    elif start=="n":  
      cal_again=False
    else:  #if user wants to start the calculator again
      clear()
      calculator()  
      
#called calculator function for the first operation
calculator()