""""
This is game finding the number

There are two levels
hard having 5 chance to find the number
easy having 10 chance to find the number

using random module
"""
import random

def number_generate():
    return random.randint(1,100)
def game_logic(local):
    number = number_generate()
    print(f"you have total chances in this level {local}")
    while local >= 0:
        print(f"Remaining chances {local}")
        user_input = int(input("Please guess the number "))
        if number == user_input:
            print(f"User number {user_input} and randon number {number}")
            print("Yeah you completed the Game Congratulation")
            break
        elif user_input < number:
            print("Enter number is less")
            local -= 1
        else:
            print("Enter number is high")
            local -= 1


def easy():
    local =10
    game_logic(local)
def hard():
    local = 5
    game_logic(local)
print("Welcome to Number Guessing game ")
print("This game will generate the number 1 to 100")
input_key= input("choose the difficulty easy or hard ").lower()

if input_key=='easy':
    easy()
elif input_key =='hard':
    hard()
else:
    print("Invalid input")
