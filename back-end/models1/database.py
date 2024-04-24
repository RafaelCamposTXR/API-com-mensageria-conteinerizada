import psycopg2

conn = psycopg2.connect(host="10.18.0.20", dbname="bd_trabalho_asa", user="postgres", password="banco123", port=5432)

cur = conn.cursor
cur.execute("CREATE TABLE IF NOT EXISTS voos (id INT PRIMARY_KEY, aeroporto_saida INT)")

cur.execute("INSERT INTO voos(id, aeroporto_saida) VALUES (0,1))")

conn.commit()

cur.close()
conn.close()
print("deu certo")