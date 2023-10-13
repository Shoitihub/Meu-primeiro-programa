from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Instala automaticamente o driver atual do navegador
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

navegador.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao\
              -org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M')
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/\
                       form/div[1]/div/div[1]/div/input').send_keys('Bruno')
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/\
                       form/div[1]/div/div[2]/div/input').send_keys('shoiti.isotani@gmail.com')
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/\
                       form/button').click()
