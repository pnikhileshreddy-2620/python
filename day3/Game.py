print("Welcome to treasure \nyour mission is to find the treasure")
print("your at the cross road.Where do you want  to go ?")

direction = input("Type Left or Right").lower()

if direction=='right':
    print('Game Over')
elif direction=='left':
    user_input = input('Enter the swim or wait')
    if user_input=='swim':
        print('Game Over')
    elif user_input=='wait':
        print('There are three doors')
        print('RED \n YELLOW \n Blue ')
        final_input = input("Enter any one option ").lower()
        if final_input=='yellow':
            print('you win')
        elif final_input=='blue':
            print("Eaten by beasts \n Game Over")
        elif final_input =='red':
            print('Burned by fire. \n Game Over')
        else:
            print('Game Over')