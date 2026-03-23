#Creates only if the file doesn't exist
file = open("cheese.txt", "x")

file.write("X marks the spot")

file.close()

#Overwrite
file = open("cheese.txt", "w")

file.write("For the W!")

file.close()

#Append
file = open("cheese.txt", "a")

file.write("A+ work")

file.close()

#Challenge
#import sys
#file_name = sys.argv[1]
#file = open(file_name, "w")
#file.close()
