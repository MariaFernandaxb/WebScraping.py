from requests_html import HTMLSession
import sqlite3

conexao = sqlite3.connect('iphones.sqlite3')
cursor = conexao.cursor()

session= HTMLSession()
url = 'https://www.olx.com.br/celulares/estado-rj?q=iphone'
resposta = session.get(url)



if (resposta.status_code !=200):
    print('Falha ao conectar')

else: 
    iphones = resposta.html.find('.olx-ad-card__link-wrapper')

    for i in iphones:
        resposta1 = session.get(i.attrs['href'])
        valores1 = resposta1.html.find('h1', first = True)
        titulo = valores1.text
        valores2 = resposta1.html.find('.ad__sc-12l420o-1')[1]
        preco = valores2.text.replace('.' , '')

        valores = [titulo, preco]
        cursor.execute('INSERT INTO CELULARES (PRODUTO, PREÇO) values (? , ?)', valores)
        


conexao.commit()
conexao.close()
     
       

