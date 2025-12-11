import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
import time


def buscar_cotacao(moeda_pesquisa):

    driver = None

    try:
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new") # Obrigatório: sem interface gráfica
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox") # Obrigatório: evita erro de permissão no Linux/Docker
        options.add_argument("--disable-dev-shm-usage") # Obrigatório: evita crash por falta de memória
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://google.com")
        wait = WebDriverWait(driver, 10)
        

        barra_pesquisa_elemento = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        barra_pesquisa_elemento.send_keys(moeda_pesquisa, Keys.ENTER)


        elemento_valor = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//span[@data-name="Real brasileiro"]/preceding-sibling::span')
            ))

        valor_texto = elemento_valor.text.replace('.', '').replace(',' , '.')
        return float(valor_texto)

    except Exception as e:
        print(f"ERRO ao buscar moeda {moeda_pesquisa}: {e}")
        raise e

    finally:
        print("Finalizando script e limpando recursos")
        if driver:
            driver.quit()


def buscar_euro():
    return buscar_cotacao("Euro hoje")


def buscar_dolar():
    return buscar_cotacao("Dólar hoje")