import sqlite3

conn = sqlite3.connect("workshop.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE movies(title, year, score)
""")

conn.commit()
conn.close()