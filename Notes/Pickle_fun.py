import pickle

age = [22, 234, 56, 89]

file = open("text.txt", "wb")
pickle.dump(age, file)
file.close()

file = open("text.txt", "rb")
new_age = pickle.load(file)
file.close()

print(new_age)