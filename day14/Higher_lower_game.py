""""
This game is just compare to value.
And increment the score
"""
import  random
from site import USER_BASE

countries_population_2025 = {
    "India": 1463870000,        # 1,463,870,000
    "China": 1416100000,        # 1,416,100,000
    "United States": 347276000, # 347,276,000
    "Indonesia": 285721000,     # 285,721,000
    "Pakistan": 255220000,      # 255,220,000
    "Nigeria": 237528000,       # 237,528,000
    "Brazil": 212812000,        # 212,812,000
    "Bangladesh": 175687000,    # 175,687,000
    "Russia": 143997000,        # 143,997,000
    "Ethiopia": 135472000       # 135,472,000
}

print("Welcome to the game ")
print("This Game about compare  the population between country ")
score =0
while True:
    country_a,country_b = random.sample(list(countries_population_2025.items()),2)
    name_a,pop_a = country_a
    name_b,pop_b =country_b
    print("Which Country having more population ")
    print(f"A {name_a}")
    print(f"B {name_b}")

    user_choice = input("Enter the option A or B").upper()
    if user_choice=='A':
        if pop_a>pop_b:
            score +=1
        else:
            print("Game is over")
            print(score)
            break
    elif user_choice =='B':
        if pop_b>pop_a:
            score+=1
        else:
            print("Game is over")
            print(score)
            break
    else:
        print("Invalid Input")
        break