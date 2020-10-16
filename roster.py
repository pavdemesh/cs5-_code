import sys
import csv
import cs50

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    exit()

house_name = sys.argv[1]

db = cs50.SQL("sqlite:///students.db")

s = db.execute('''SELECT first, middle, last, birth FROM students WHERE house = ? ORDER  BY last, first''', (house_name,))

for row in s:
    if row['middle'] is None:
        print(f"{row['first']} {row['last']}, born {row['birth']}")
    else:
        print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")
