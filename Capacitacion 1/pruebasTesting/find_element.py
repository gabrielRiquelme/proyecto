from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

#Declaracion de driver#
path_to_chromedriver = r'C:\Users\gabri\PycharmProjects\pruebasTesting\Drivers\chromedriver.exe'
service = Service(path_to_chromedriver)
driver = webdriver.Chrome(service=service)
driver.get("https://google.com")
driver.maximize_window()

#Automatizacion#
busqueda = driver.find_element(By.ID, 'APjFqb')
boton = driver.find_element(By.NAME, 'btnK')
link = driver.find_element(By.ID, 'ID=SERP,5200.2')

time.sleep(2)

busqueda.send_keys('Promedios')

time.sleep(2)

boton.click()

time.sleep(2)

link.click()

time.sleep(150)