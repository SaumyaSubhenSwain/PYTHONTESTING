import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--headless")
chrome_Options.add_argument("--ignore-certificate-errors")

service_obj = Service(r"D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_Options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")

time.sleep(2)
