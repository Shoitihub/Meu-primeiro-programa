from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Instala automaticamente o driver atual do navegador
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

navegador.get('https://www.facebook.com/')
# Find the username and password input fields and login button using better locators
username_field = navegador.find_element(By.ID, 'email')
password_field = navegador.find_element(By.ID, 'pass')
login_button = navegador.find_element(By.NAME, 'login')

# Enter the username and password and click the login button
username_field.send_keys('shoiti.isotani@gmail.com')
password_field.send_keys('Shoiti2605')
login_button.click()

