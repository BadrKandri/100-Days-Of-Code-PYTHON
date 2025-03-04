from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Only show fatal errors, hide warnings and info
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after execution

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
# choose language
language_select = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'langSelect-EN')]")))
language_select.click()

timeout = time.time() + 1

click_cookie=driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
cookies = driver.find_element(By.XPATH, '//*[@id="cookies"]')
number_cookies=int(cookies.text.split()[0]) 
# elements to buy
cursor=driver.find_element(By.XPATH, '//*[@id="product0"]')

while True:
    click_cookie.click()
    if time.time() > timeout:    
        cursor.click()       
        timeout = time.time() + 1
# end