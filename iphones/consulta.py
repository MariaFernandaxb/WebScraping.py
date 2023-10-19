import sqlite3

conexao = sqlite3.connect('iphones.sqlite3')
cursor = conexao.cursor()

resultados = cursor.execute('SELECT PRODUTO,PREÇO FROM CELULARES ORDER BY PREÇO ASC')

for linha in resultados:
    print(linha)
    
conexao.close()
