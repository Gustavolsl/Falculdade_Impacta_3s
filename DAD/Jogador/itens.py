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

class ItemNaoExisteException(Exception):
    pass

def consultar_item(id):
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM item WHERE id = (?)"
    cursor.execute(sql,[id])
    item = cursor.fetchone()
    if item == None:
        raise ItemNaoExisteException
    cursor.close()
    #print(item,id)
    return {'id':item[0], 'nome':item[1], 'tipo':item[2], 'fisico':item[3],'magia':item[4], 'agilidade':item[5], 'emUso':item[6]}

    