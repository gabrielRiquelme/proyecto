from selenium import webdriver
from selenium.webdriver.edge.service import Service

import time
service = Service(executable_path="Drivers/msedgedriver.exe")
controlador = webdriver.Edge(service=service)

controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F")


usuario = controlador.find_element_by_id("form-group--1")
passw = controlador.find_element_by_id("form-group--3")
boton = controlador.find_element_by_id("")


usuario.send_keys("gabrielcabj986@gmail.com")

passw.send_keys("Prueba-128910")

boton.click()

controlador.quit()