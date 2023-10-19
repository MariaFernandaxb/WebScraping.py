import sqlite3

conexao = sqlite3.connect('passaros.sqlite3')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE PASSAROS (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME TEXT(50)
)
''')

conexao.commit()
conexao.close()