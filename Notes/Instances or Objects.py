import random

class Dog:
    info = "A furry creature that barks."

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name


dog1 = Dog("Leo")
dog2 = Dog("Simba")

print(dog1.lucky_number)
print(dog2.lucky_number)


print(dog1.name)
print(dog2.name)

class Computer:
    def __init__(self, brand):
        self.brand = brand

computer1 = Computer("Microsoft")
print(computer1.brand)