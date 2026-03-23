#Read
file = open("cheese.txt", "r")
lines = file.readlines()
file.close()

#Edit

lines.insert(0, "I like cheese\n")

lines[1] = "Hello friend!\n"

lines[-1] = lines[-1] + "\n"
lines.append("Goodbye!\n")

#Write
file = open("cheese.txt", "w")
file.writelines(lines)
file.close()