from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Inicializar el servicio y el controlador de Chrome
service = Service(executable_path="Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Datos#
emailDa = "gabrielcabj986@gmail.com"
passDa = "Prueba-128910"

# Abrir la página de inicio de sesión de Udemy
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fuser%2Fforgot-password%2F")

# Esperar un momento para que la página cargue completamente
time.sleep(5)

# Encontrar elementos por sus selectores CSS
email = driver.find_element(By.CSS_SELECTOR, ".ud-text-input.ud-text-input-large.ud-text-md.ud-compact-form-control")
passw = driver.find_element(By.CSS_SELECTOR, ".ud-compact-form-control-container input[type='password']")


# Ingresar el correo electrónico y la contraseña
email.send_keys(emailDa)
passw.send_keys(passDa)

# Hacer clic en el botón de inicio de sesión
button = driver.find_element(By.CSS_SELECTOR, "ud-btn")
button.click()

# Esperar un momento después de hacer clic
time.sleep(5)

# Cerrar el navegador al finalizar
driver.quit()
