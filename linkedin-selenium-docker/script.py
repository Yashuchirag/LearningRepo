import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.linkedin.com/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_field = driver.find_element(By.ID, "password")

# Use credentials from env
username_field.send_keys(os.getenv("LINKEDIN_USER"))
password_field.send_keys(os.getenv("LINKEDIN_PASS"))

sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()

print("Login attempted.")
driver.quit()