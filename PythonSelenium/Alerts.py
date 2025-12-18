from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name="Saumya"
service_obj = Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Saumya")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText= alert.text
print(alertText)

assert name in alertText
alert.accept()
# alert.dismiss()