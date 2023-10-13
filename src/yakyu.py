from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
url = 'https://brazil.wbsc.org/en/calendar'
pagina = requests.get(url, headers=headers)
site = BeautifulSoup(pagina.content, 'html.parser')
calendario = site.find_all("table", class_="table table-condensed table-desktop") 
torneios = calendario[0].find_all("td", class_="name")
for p, i in enumerate(torneios):
  print(f'[{p+1}] {i.find("a").get_text().strip()}')
escolha = int(input('Qual dos torneios voce quer ver? '))
print(torneios[escolha-1])
