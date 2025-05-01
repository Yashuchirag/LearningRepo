from h5py.h5ds import detach_scale
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

website = 'https://www.football-data.co.uk/'
path = "D:\Software\Chrome\chrome-win64\chrome-win64\chrome.exe"

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if 'Books' in link.get_attribute('innerHTML'):
        link.click()
        break

book_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-column-wrap')][.//h2text()[contains(.,'Books')]]")
for book_link in book_links:
    book_link.click()