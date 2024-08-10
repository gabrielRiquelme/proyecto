from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Inicializar el servicio para el controlador de Chrome
service = Service(executable_path="Drivers/chromedriver.exe")
controlador = webdriver.Chrome(service=service)

# Navegar a la página de inicio de sesión de Udemy
controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F")

# Esperar a que los elementos estén disponibles
time.sleep(3)

# Encontrar los elementos de entrada
usuario = controlador.find_element(By.NAME, "email")
passw = controlador.find_element(By.NAME, "password")
boton = controlador.find_element(By.CSS_SELECTOR, ".ud-btn.ud-btn-large.ud-btn-brand.ud-heading-md.helpers--auth-submit-button--W3Tqk")

# Ingresar el nombre de usuario y la contraseña
usuario.send_keys("gabrielcabj986@gmail.com")
passw.send_keys("Prueba-128910")

# Esperar un poco antes de hacer clic en el botón
time.sleep(3)
boton.click()

# Esperar antes de cerrar el navegador
time.sleep(5)
controlador.quit()
