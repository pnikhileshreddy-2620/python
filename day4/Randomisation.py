import  random
import my_module
"""
The random module in Python is a built-in module used to generate pseudo-random numbers and make random choices. 
It’s super common in games 🎮, 
simulations, testing, data sampling, and simple probability tasks.
"""

print(random.random())

print(random.randint(1,10))
print(random.randrange(1,10,2))
print(my_module.i)

coins =["Head","Talis"]
print(random.choice(coins))