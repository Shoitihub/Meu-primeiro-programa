from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import getpass

service = Service(ChromeDriverManager().install())

options = Options()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=service, options=options)

id = 'shoiti.isotani@gmail.com'
key = getpass.getpass('Digite sua senha - ')
driver.set_page_load_timeout(10)
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.ID, "email").send_keys(id)
driver.find_element(By.ID, "pass").send_keys(key)
driver.find_element(By.NAME, "login").click()
driver.implicitly_wait(1)
if driver.title == "Facebook":
    driver.get("https://www.facebook.com/events/birthdays")
    driver.implicitly_wait(5)
    message = driver.find_elements('xpath', "//textarea[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
    for text in message:
        text.send_keys("Feliz aniversário")
        text.send_keys(Keys.RETURN)
else:
    print('Informação inválida. Execute o código novamente')
    driver.quit()