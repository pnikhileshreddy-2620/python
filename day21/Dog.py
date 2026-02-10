from python.day21.Animal import Animal


class Dog(Animal):
    def speak(self):
        return 'woooo'
dog =Dog('dog')
print(dog.name)
print(dog.speak())
