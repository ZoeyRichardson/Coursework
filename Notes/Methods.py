import random

class Dog:
    info = "A furry creature that barks."

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"Woof! My name is {self.name} and my number is {self.lucky_number}")


dog1 = Dog("Leo")
dog2 = Dog("Simba")

dog1.bark()
dog2.bark()

class Computer:
    def __init__(self, brand):
        self.brand = brand

    def age(self):
        print(f"I'm a {self.brand} computer and I'm 3 years old.")

computer1 = Computer("Microsoft")
computer2 = Computer("Apple")
print(computer1.brand)
computer1.age()
computer2.age()