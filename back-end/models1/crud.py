import psycopg2

conn = psycopg2.connect(host="localhost", dbname="bd_trabalho_asa", user="postgres", password="bancosenha", port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS voos (
            id INT PRIMARY KEY, 
            aeroporto_saida INT, 
            aeroporto_chegada INT, 
            data_saida VARCHAR(80), 
            data_chegada VARCHAR(80),
            preco FLOAT,
            passageiros INT
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS aeroportos (
            id INT PRIMARY KEY, 
            nome VARCHAR(80), 
            cidade VARCHAR(80), 
            estado VARCHAR(2)
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS compras (
            id INT PRIMARY KEY, 
            id_voo INT,  
            data_compra VARCHAR(80)
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id INT PRIMARY KEY, 
            nome VARCHAR(50), 
            email VARCHAR(20), 
            senha VARCHAR(40)
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS reservas (
            id INT PRIMARY KEY, 
            id_voo INT, 
            passageiros INT, 
            total FLOAT
            );""")


#
# retorna voos
#

def get_voos():
    cur.execute("""
            SELECT * FROM voos;
            """)
    conn.commit()
    resposta = cur.fetchall()
    print("deu certo")
    return resposta


#
# retorna aeroportos
#

def get_aeroportos():
    cur.execute("""
            SELECT * FROM aeroportos;
            """)
    print(cur.fetchall())
    conn.commit()
    print("deu certo")

#
# retorna aeroportos de destino de acordo com o aeroporto de origem
#

def get_aeroportos_por_origem(origem):
    cur.execute(f"""
        SELECT DISTINCT *
        FROM aeroportos
        WHERE cidade = '{origem}';
    """)
    valor = cur.fetchall()
    conn.commit()
    return valor

#
# retorna voo em certa data
#

def get_voo_por_data(data):
    cur.execute(f"""
        SELECT DISTINCT *
        FROM voos
        WHERE data_saida = '{data}';
    """)
    print(cur.fetchall())
    valor = cur.fetchall()
    conn.commit()
    return valor

#
# efetua a pesquisa de voos e retorna uma lista de voos com a
# menor tarifa disponível no momento para o número de passageiros informados
#

def get_voos_menor_tarifa(passageiros):
    cur.execute(f"""
        SELECT *
        FROM voos
        ORDER BY preco;
    """,)
    voo = cur.fetchone()
    conn.commit()
    if voo:
        preco_voo = float(voo['preco'])
        total = passageiros * preco_voo
        print("O total é %.2f", total)
        return voo
    else:
        return None, None


#
# efetua a reserva e a compra dos voos e tarifas selecionados e
# retorna o localizador da reserva e o número de e-tickets
#

def efetuar_compra(id_voo, passageiros, total):
    cur.execute(f"""
        INSERT INTO reservas (id_voo, passageiros, total)
        VALUES ({id_voo}, {passageiros}, {total})
        RETURNING id;
    """)  
    id_reserva = cur.fetchone()[0]
    conn.commit()
    return f"Seu localizador de reserva é: {id_reserva} e foram criados {passageiros} e-tickets"