
print("before")

try:
    #4 / 0
    print(age)
except NameError as e:
    print("We had a name error!")
    print(e)
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print("Something went wrong.")

class CheeseError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("The word has to have at least 1 letter!")
    return word.upper()

print(upper_fun(""))

print("after")