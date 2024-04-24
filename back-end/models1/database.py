import psycopg2

conn = psycopg2.connect(host="", dbname="", user="", password="", port=0)

cur = conn.cursor
cur.execute("CREATE TABLE IF NOT EXISTS teste (id INT PRIMARY_KEY)")

conn.commit()

cur.close()
conn.close()