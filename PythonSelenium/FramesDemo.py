import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service("D:\\Driver\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)

# Switch to iframe
driver.switch_to.frame("mce_0_ifr")

# Locate the <body> inside iframe
editor= driver.find_element(By.ID, "tinymce")

# Instead of .clear(), use CTRL+A + DELETE (works reliably for TinyMCE)
editor.send_keys(Keys.CONTROL + "a")
editor.send_keys(Keys.DELETE)
time.sleep(4)
# Now type your text
editor.send_keys("I am able to automate frames")

# Switch back to main page
driver.switch_to.default_content()

# Print the h3 heading text
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
