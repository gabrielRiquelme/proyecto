from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F&persist_locale")

link_recuperacion = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot Password")

link_recuperacion.click()

time.sleep(5)




