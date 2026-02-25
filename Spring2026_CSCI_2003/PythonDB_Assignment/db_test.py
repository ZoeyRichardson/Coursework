import sqlite3
con = sqlite3.connect("StudentRecords.db")
cur = con.cursor()
#cur.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, major TEXT)")
#cur.execute("INSERT INTO students VALUES (1, 'Oliver', 19, 'Political Science')")
#cur.execute("INSERT INTO students VALUES (2, 'Felicity', 18, 'Computer Science')")
#cur.execute("INSERT INTO students VALUES (3, 'Barry', 17, 'Forensic Science')")
#cur.execute("INSERT INTO students VALUES (4, 'Kara', 20, 'Journalism')")
#cur.execute ("INSERT INTO students VALUES (5, 'Cisco', 21, 'Engineering')")
con.commit()
cur.execute("SELECT name, age, major FROM students")
rows = cur.fetchall()
for r in rows:
    print(r)

choice = input("Do you want to add a new student? (yes/no): ")

if choice == "yes":
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    major = input("Enter the student's major: ")
    cur.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    con.commit()
    print("Mission accomplished. Student added to the database!")
