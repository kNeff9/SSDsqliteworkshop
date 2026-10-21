import sqlite3

conn = sqlite3.connect("workshop.db")
cur = conn.cursor()

cur.execute("""
    INSERT INTO movies VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

cur.execute("""
    SELECT * FROM movies
""")

res = cur.fetchall()

for item in res:

    print(item)

conn.commit()
conn.close()