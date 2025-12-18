from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)