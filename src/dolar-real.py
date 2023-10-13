import requests
from bs4 import BeautifulSoup
from datetime import date

#Informa a versao do navegador para obter dados
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
pagina = requests.get("https://www.google.com/search?q=cotacao+dolar", headers=headers)
site = BeautifulSoup(pagina.content, 'html.parser')
#Localiza no site a cotacao do dolar
cotacao_dolar = (site.find("span", class_="SwHCTb"))
print(f'''{date.today()}
1 dolar equivale a {cotacao_dolar.get_text()} reais''')
#Pega apenas o valor da cotacao
cotacao_dolar = cotacao_dolar['data-value']
dolar = float(input('Dolar(U$)'))
print(f'U${dolar} = R${dolar*float(cotacao_dolar):.2f}')
