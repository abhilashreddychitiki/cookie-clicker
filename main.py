import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Correct driver initialization
driver = uc.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Allow time for initial loading
time.sleep(5)

# Try to select English language if it appears
try:
    lang_select = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    lang_select.click()
    print("Language selected.")
except:
    print("Language selection not found, continuing...")

# Wait for the game to fully load
time.sleep(5)

# Find the cookie element
cookie = driver.find_element(By.ID, "bigCookie")

# Click the cookie with random intervals
while True:
    cookie.click()
    # time.sleep(random.uniform(0.1, 0.3))  # Random delay to simulate human clicks
