import sys
import csv
import cs50

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    exit()

csv_fname = sys.argv[1]

db = cs50.SQL("sqlite:///students.db")
db.execute("DELETE FROM students")

with open(csv_fname, "r") as fhand:
    reader = csv.DictReader(fhand)
    for row in reader:
        name = row["name"].split()
        if len(name) == 2:
            db.execute('''INSERT INTO students (first, middle, last, house, birth) VALUES
            (?, NULL, ?, ?, ?)''', (name[0], name[1], row["house"], row["birth"]))
        else:
            db.execute('''INSERT INTO students (first, middle, last, house, birth) VALUES
                        (?, ?, ?, ?, ?)''', (name[0], name[1], name[2], row["house"], row["birth"]))
