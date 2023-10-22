from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Instala automaticamente o driver atual do navegador
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)
navegador.get('https://www.facebook.com/')
email = navegador.find_element(By.ID, 'email')
senha = navegador.find_element(By.ID, 'pass')
login = navegador.find_element(By.NAME, 'login')
email.send_keys('shoiti.isotani@gmail.com')
senha.send_keys('Shoiti2605')
login.click()

