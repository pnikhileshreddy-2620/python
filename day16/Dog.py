class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age =age
    def bark(self):
        print("Wooaf")

dog1 = Dog("LLED",20)
# dog1 is a new dog object created using Dog class
# Passing the data in Dog(here)
dog2 =Dog("PH",20)
# dog2 is a new dog object created using Dog class
print(dog1)
print(dog2)

# printing the attributes of the dog

print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog2.age)
dog1.bark()
dog2.bark()

