import psycopg2

conn = psycopg2.connect(host="localhost", dbname="bd_trabalho_asa", user="postgres", password="bancosenha", port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS voos (
            id INT PRIMARY KEY, 
            aeroporto_saida INT, 
            aeroporto_chegada INT, 
            data_saida VARCHAR(80), 
            data_chegada VARCHAR(80),
            preco FLOAT
            );""")



# retorna voos
def get_voos():
    cur.execute("""
            SELECT * FROM voos;
            """)
    conn.commit()
    resposta = cur.fetchall()
    print("deu certo")
    return resposta



# retorna aeroportos
def get_aeroportos():
    cur.execute("""
            SELECT * FROM aeroportos;
            """)
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()
    print("deu certo")


# retorna aeroportos de destino de acordo com o aeroporto de origem
def get_aeroportos_por_origem(origem):
    cur.execute(f"""
        SELECT DISTINCT a.*
        FROM aeroportos a
        INNER JOIN voos v ON a.id = v.aeroporto_chegada
        WHERE v.aeroporto_saida = {origem};
    """)
    print(cur.fetchall())
    conn.commit()
    print("deu certo")


# retorna voo em certa data
def get_voo_por_data(data):
    cur.execute("""
        SELECT DISTINCT v.*
        FROM voos v
        WHERE v.data_saida = %s;
    """, (data,))
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()
    print("deu certo")


# efetua a pesquisa de voos e retorna uma lista de voos com a
# menor tarifa disponível no momento para o número de passageiros informados
def get_voos_menor_tarifa(aeroporto_saida, aeroporto_chegada, data_saida, data_chegada, passageiros):
    cur.execute("""
        SELECT v.*
        FROM voos v
        WHERE v.aeroporto_saida = %s 
            AND v.aeroporto_chegada = %s 
            AND v.data_saida >= %s 
            AND v.data_chegada <= %s 
            AND v.passageiros >= %s
        ORDER BY v.preco
        LIMIT 1;
    """, (aeroporto_saida, aeroporto_chegada, data_saida, data_chegada, passageiros))
    result = cur.fetchall()
    if result:
        print(result[0])  # Imprime o voo com a menor tarifa
    else:
        print("Nenhum voo encontrado para os critérios fornecidos")
    conn.commit()
    cur.close()
    conn.close()


# efetua a reserva e a compra dos voos e tarifas selecionados e
# retorna o localizador da reserva e o número de e-tickets