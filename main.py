import sqlite3

conn = sqlite3.connect("workshop.db")
cur = conn.cursor()


cur.execute("""
    SELECT * FROM workouts
""")

res = cur.fetchall()

for item in res:

    print(item)

conn.commit()
conn.close()