import psycopg2

conn = psycopg2.connect(host="localhost", dbname="bd_trabalho_asa", user="postgres", password="banco123", port=5432)
cur = conn.cursor()


def get_voos():
    cur.execute("""
            SELECT * FROM voos;
            """)
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()
    print("deu certo")

def get_aeroportos():
    cur.execute("""
            SELECT * FROM aeroportos;
            """)
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()
    print("deu certo")