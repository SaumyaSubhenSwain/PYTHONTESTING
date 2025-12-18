import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []
service_obj = Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

#Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']")

# collect all  veggie names --> BrowserSortedveggieList  (B,A,C)
veggieWebElements= driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)
    # print(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#sort this BrowserSortedveggieList --> newSortedList  -> (A,B,C)
browserSortedVeggies.sort()
time.sleep(3)
print(browserSortedVeggies)
print(originalBrowserSortedList)
assert browserSortedVeggies == originalBrowserSortedList

