import sqlite3

conn = sqlite3.connect("workshop.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE workouts(id, type, weight, date)
""")

conn.commit()
conn.close()