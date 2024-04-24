import psycopg2

conn = psycopg2.connect(host="localhost", dbname="bd_trabalho_asa", user="postgres", password="banco123", port=5432)

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS voos (
            id INT PRIMARY KEY, 
            aeroporto_saida INT, 
            aeroporto_chegada INT, 
            data_saida DATE, 
            data_chegada DATE,
            preco FLOAT
            );""")

cur.execute("""INSERT INTO voos(id, aeroporto_saida, aeroporto_chegada, data_saida, data_chegada, preco) VALUES 
            (0, 1, 2, '2024-04-23', '2024-05-23', 180), 
            (1, 4, 5, '2024-04-23', '2024-05-23', 180),
            (2, 5, 3, '2024-04-23', '2024-05-23', 180),
            (3, 7, 6, '2024-04-23', '2024-05-23', 180);""")

cur.execute("""SELECT * FROM voos;""")
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()
print("deu certo")