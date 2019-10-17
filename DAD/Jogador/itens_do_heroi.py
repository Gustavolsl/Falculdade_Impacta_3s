import sqlite3     
connection = sqlite3.connect("rpg.db")
create_sql = """
CREATE TABLE IF NOT EXISTS Heroi(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    fisico INTEGER NOT NULL,
    magia INTEGER NOT NULL,
    agilidade INTEGER NOT NULL
)
"""
cursor = connection.cursor()
#2o passo: pegar o cursor
cursor.execute(create_sql)
#3o passo: cursor.execute passando uma string de sql
connection.commit()
#4o passo: fazer o commit (se for uma query que altera o banco)
connection.close()
#5o passo: fechar a conexao

def consulta_itens_por_heroi(idHeroi):
    list_itens = []
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM ItemDoHeroi WHERE idHeroi = (?)"
    cursor.execute(sql, [idHeroi])
    retorno= cursor.fetchall()
    tamanho = len(retorno)
    count = 0
    if tamanho >= 1:
        for i in retorno:
            list_itens.append({'id':i[0],'idItem':i[1],'idHeroi':i[2]})
            count += 1
    #print(list_itens,idHeroi)
    return list_itens