from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

#Instala automaticamente o driver atual do navegador
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

navegador.get('https://meupc.net/login')
sleep(1)
navegador.find_element('xpath', '/html/body/main/section/div/div/form/section/\
                       div[3]/input').send_keys('shoiti')#usuário
sleep(1)
navegador.find_element('xpath', '/html/body/main/section/div/div/form/section/\
                       div[4]/span/input').send_keys('Shoiti@2605')#senha
sleep(1)
navegador.find_element('xpath', '/html/body/main/section/div/div/form/section/\
                       div[5]/button[2]').click()