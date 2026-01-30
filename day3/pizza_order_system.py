print("welcome to pizza order system ")
prizes ={
    "L":25,
    "M":20,
    "S":15
}
pepperoni ={
    "Y":2,
    "N":0
}
extra_chess={
    "Y":1,
    "N":0
}

size =input("what is the size of pizza S<M<L ").upper()
_pepperoni = input("Do you want pepperoni Y or N ").upper()
_Extra_chess = input("Do you want Extra chess Y or N ").upper()

if _pepperoni=='Y' and size=='S':
    print("Final Bill is " ,prizes[size]+pepperoni[_pepperoni]+extra_chess[_Extra_chess])
elif _pepperoni=='Y' and size =='L' or size=='M':
    print("Final Bill is ",prizes[size] + pepperoni[_pepperoni]+1 + extra_chess[_Extra_chess])