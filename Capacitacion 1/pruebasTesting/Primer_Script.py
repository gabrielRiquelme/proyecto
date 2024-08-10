from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Asegúrate de que la ruta al controlador sea correcta
service = Service(executable_path="Drivers/msedgedriver.exe")

driver = webdriver.Edge(service=service)
# Maximiza la ventana del navegador
driver.maximize_window()

# Navega a la página de inicio de sesión de Instagram
driver.get("https://www.instagram.com/")

