from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
from shutil import move

dir_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv()

# set url
url = "https://opencaselist.com"

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.headless = True

download_path = os.path.join(dir_path, 'selenium_downloads')
prefs = {
   "download.default_directory": download_path,
   "savefile.default_directory": download_path,
   "profile.managed_default_content_settings.images": 2
}

chrome_options.add_experimental_option('prefs', prefs)

chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("prefs", prefs)
service = Service(os.getenv('driverpath'))
driver = webdriver.Chrome(service=service, options=chrome_options)

# login
def scrape(driver):
   username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'username')))
   password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
   username.send_keys(os.getenv('opencluser'))
   password.send_keys(os.getenv('openclpass'))

   driver.find_element(By.CLASS_NAME, "pure-button").click()
   time.sleep(2)

   driver.find_element(By.XPATH, '//a[@href="/openev"]').click()
   

driver.get(url)
scrape(driver)

# Open the webpage
for year in range(2013, 2024):

   destination = os.path.join(download_path, str(year))
   os.mkdir(destination)

   driver.get(f"https://opencaselist.com/openev/{year}")
   print(f'Loaded {year} page')
   docs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_link_1jy1d_8')))
   # docs = driver.find_elements(By.CLASS_NAME, '_link_1jy1d_8')
   # print(docs)
   for doc in docs:
      doc.click()
      print(f'Downloading {doc.text}.docx')
      downloaded_file = os.path.join(download_path, doc.text+'.docx')
      while not os.path.exists(downloaded_file):
         time.sleep(1)
      destination_file = os.path.join(destination, doc.text+'.docx')
      move(downloaded_file, destination_file)
      print(f'Saving {downloaded_file} to {year} directory')
      







         
