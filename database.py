import sqlite3
import datetime 


def criar_tabela():
    with sqlite3.connect("my_database.db") as connection:

        cursor = connection.cursor()

        sql = '''
        CREATE TABLE IF NOT EXISTS historico(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor FLOAT,
            data TIMESTAMP
        )
        '''

        cursor.execute(sql)

        connection.commit()

        print("Tabela criada!")

def salvar_valor(valor_dolar):
    with sqlite3.connect("my_database.db") as connection:

        cursor = connection.cursor()

        data = datetime.datetime.now()
        
        sql = '''
        INSERT INTO historico(valor, data) VALUES(?, ?)
        '''

        cursor.execute(sql, (valor_dolar, data))

        connection.commit()
        print(f"Valor {valor_dolar} salvo com sucesso!")


