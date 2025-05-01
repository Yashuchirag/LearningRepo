from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.maximize_window()


# Wait until the sign-in button is visible and click it
wait = WebDriverWait(driver, 10)

username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_field = driver.find_element(By.ID, "password")

# --- Enter credentials ---
username_field.send_keys("chiragchandrashekar@gmail.com")
password_field.send_keys("***********")

# --- Click the Sign In button ---
sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()
