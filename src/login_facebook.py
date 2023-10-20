from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Instala automaticamente o driver atual do navegador
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

navegador.get('https://www.facebook.com/')
navegador.find_element('xpath', '//*[@id="email"]').send_keys('shoiti.isotani@gmail.com')#usuário
navegador.find_element('xpath', '//*[@id="pass"]').send_keys('Shoiti2605')#senha
navegador.find_element('xpath', '//*[@id="u_0_5_v1"]').click()
