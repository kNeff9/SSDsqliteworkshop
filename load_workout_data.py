import sqlite3
import csv

conn = sqlite3.connect("workshop.db")
cur = conn.cursor()

with open("data/workout_data.txt", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    for row in reader:

        # Each row is an entry in workout_data
        # It is structured as id,exercise_type,weight_used,date

        id = int(row[0])
        exercise_type = row[1]
        weight_used = int(row[2])
        date = row[3]

        cur.execute("""
            INSERT INTO workouts (id, type, weight, date)
            VALUES (?, ?, ?, ?)
        """, (id, exercise_type, weight_used, date))

conn.commit()
conn.close()