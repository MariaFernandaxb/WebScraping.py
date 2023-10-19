import sqlite3

conexao = sqlite3.connect('iphones.sqlite3')
cursor = conexao.cursor()


cursor.execute('''
CREATE TABLE CELULARES (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    PRODUTO TEXT(30),
    PREÇO INTEGER
)
''')
