"""
Game Rock Paper scissor
Using two parameter
One is system input.
Other is user input.
Rock wins on scissor
scissor win on paper
paper win on rock
"""

import  random



system=["ROCK","PAPER","SCISSORS"]
system_input = random.choice(system)
print("\n ROCK \n PAPER \n SCISSOR ")
user_input = input("Enter anything in the game ").upper()
if system_input==user_input:
    print("Tie")
elif system_input=='ROCK' and user_input=='PAPER':
    print("USER WIN")
elif system_input=='ROCK' and user_input=='SCISSORS':
    print('SYSTEM WIN')
elif system_input=='SCISSORS' and user_input=='PAPER':
    print("SYSTEM WIN")
elif system_input=='SCISSORS' and user_input=='ROCK':
    print('USER WIN')
elif system_input=='PAPER' and user_input=='ROCK':
    print("SYSTEM  WIN")
elif system_input=='PAPER' and user_input=='SCISSORS':
    print('USER WIN')
else:
    print("Hey, Please check the input")

