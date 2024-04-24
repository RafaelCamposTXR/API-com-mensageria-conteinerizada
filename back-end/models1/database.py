import psycopg2

conn = psycopg2.connect(host="10.18.0.20", dbname="bd_trabalho_asa", user="postgres", password="banco123", port=5432)

cur = conn.cursor
cur.execute("CREATE TABLE IF NOT EXISTS teste (id INT PRIMARY_KEY)")

conn.commit()

cur.close()
conn.close()
print("deu certo")