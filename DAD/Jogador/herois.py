def consultar_heroi(id):
    connection = sqlite3.connect("rpg.db")

    cursor = connection.cursor()

    sql = "SELECT * FROM heroi WHERE id = (?)"
    cursor.execute(sql, [id])
    
    
    heroi = cursor.fetchone()

    connection.close()

