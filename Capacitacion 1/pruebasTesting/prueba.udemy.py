from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

# Especifica el path completo al chromedriver
path_to_chromedriver = r'C:\Users\gabri\PycharmProjects\pruebasTesting\Drivers\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()


# Configura el servicio del ChromeDriver
service = Service(path_to_chromedriver)


# Inicializa el navegador con el servicio
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F')

prefs = {"profile.default_content_settings.popups": 2}
chrome_options.add_experimental_option("prefs", prefs)


#Iniciar sesion#
#Ingreso Email#
username = webdriverWait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
username.clear()
username.send_keys('gabrielcabj986@gmail.com')

#Ingreso Pass#
password = webdriverWait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
password.clear()
password.send_keys('Prueba-128910')


#click boton inicia sesion#
boton = webdriverWait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
boton.click()





time.sleep(500)
#Cerrar el navegador
driver.quit()
