from requests_html import HTMLSession
import sqlite3

conexao = sqlite3.connect('passaros.sqlite3')
cursor = conexao.cursor()

session = HTMLSession()
url = 'https://turismodenatureza.com.br/passaros-mais-bonitos-do-brasil/'
resposta = session.get(url)

lista = resposta.html.find('.elementor-widget-container h3')


for passarinho in lista[0:50]:
    nome = passarinho.text

    print(nome)

    cursor.execute('INSERT INTO PASSAROS (NOME) VALUES (?)' , [nome])

conexao.commit()
conexao.close()