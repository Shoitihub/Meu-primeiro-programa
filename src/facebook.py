from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from dotenv import load_dotenv
import ast
import time
from datetime import datetime, date
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR')# Set the locale to Portuguese


def page_has_loaded(driver, sleep_time=2):
    '''
    Waits for page to completely load by comparing current page hash values.
    '''
    def get_page_hash(driver):
        '''
        Returns html dom hash
        '''
        dom = driver.find_element(By.TAG_NAME, 'html').get_attribute('innerHTML')
        dom_hash = hash(dom.encode('utf-8'))
        return dom_hash

    page_hash = 'empty'
    page_hash_new = ''
    # Use WebDriverWait for more intelligent waiting
    try:
        WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.TAG_NAME, 'html')))
    except Exception as e:
        logging.warning(f"Error waiting for staleness: {e}")
    # comparing old and new page DOM hash together to verify the page is fully loaded
    while page_hash != page_hash_new:
        page_hash = get_page_hash(driver)
        time.sleep(sleep_time)
        page_hash_new = get_page_hash(driver)
        logging.info('<page_has_loaded> - page not loaded')
    logging.info('<page_has_loaded> - page loaded: {}'.format(driver.current_url))

def main():
    # Inicio do Programa
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(service=service, options=options)
    # Dados do arquivo .env
    id = os.environ.get('FACEBOOK_USER')
    key = os.environ.get('FACEBOOK_PASSWORD')
    driver.set_page_load_timeout(5)
    try:
        driver.get("https://facebook.com/")
        driver.maximize_window()
        page_has_loaded(driver, sleep_time = 2)
        driver.find_element(By.NAME, "email").send_keys(id)
        driver.find_element(By.NAME, "pass").send_keys(key)
        driver.find_element(By.NAME, "login").click()
        page_has_loaded(driver, sleep_time = 2)
        driver.get("https://facebook.com/friends/birthdays")
        page_has_loaded(driver, sleep_time = 2)
        #Procura o grid pelo id 
        xpath = "//div[contains(@id,'mount_0_0')]"
        elem = driver.find_element(By.XPATH, xpath)
        texto = elem.text
        n = str.find(texto, 'Aniversariantes do dia')
        n2 = str.find(texto, 'Aniversários recentes')
        n3 = str.find(texto, 'Próximos aniversários')
        #Verifica se tem aniversariantes hoje
        if n > 0:
            if n2 > 0:
                temp = texto[n:n2]
            else:
                if n3 > 0:
                    temp = texto[n:n3]
                else:
                    temp = texto[n:]
            temp = temp.replace('\n', '*')
            nomes = []
            controle=True
            while controle:
                n = str.find(temp, '*')
                temp = temp[n+1:]
                n2 = str.find(temp, '*')
                if n2 > 0:
                    nomes += [temp[:n2]]
                    n = str.find(temp, 'Escreva')
                    temp = temp[n:]
                else:
                    controle=False
            # Escevere no Mural do aniversariante
            for i, nome in enumerate(nomes):
                elems = elem.find_elements(By.TAG_NAME, 'p')
                elems[i].send_keys(f'{nome}, Feliz Aniversario!')
                action = ActionChains(driver)
                action.send_keys(Keys.ENTER).perform()
                print(f'Escrito no mural de: {nome}')
        else:
            controle=False
            print(f'Não temos aniversariante no dia de hoje: {date.today()}')
            driver.close()
        driver.close()
        print('FIM!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
