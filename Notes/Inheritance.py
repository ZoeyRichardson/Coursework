import random

class Animal:
    info = "A living organism that feeds on organic matter."

    def __init__(self, name):
        print("An animal is born!")
        self.name = name

class Dog(Animal):
    info = "A furry creature that barks!"

    def __init__(self, name):
        super().__init__(name)
        print("A dog is born!")
        self.lucky_number = random.randint(1,10)
        self.fur = ""

    def bark(self):
        print(f"Woof! My name is {self.name} and my number is {self.lucky_number}")


class Miniature_Dachshund(Dog):

    def __init__(self, name):
        super().__init__(name)
        print("A miniature dachshund is born!")
        


dog1 = Miniature_Dachshund("Leo")

#print(dog1.info)
#dog2 = Dog("Simba")

#dog1.bark()
#dog2.bark()