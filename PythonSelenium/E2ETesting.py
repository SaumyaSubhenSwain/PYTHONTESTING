from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedProductName= input("Enter a product name")
country = input("Enter a country name")

service_obj = Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#  //a[contains(@href,'shop')]     a[href*='shop']---> CSS
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products= driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    actualProductName= product.find_element(By.XPATH,"div/h4/a").text
    if actualProductName == expectedProductName:
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()    #//button[contains(text(),'Checkout')]
driver.find_element(By.ID,"country").send_keys(country)
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, country)))
driver.find_element(By.LINK_TEXT,country).click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successTest= driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successTest
print(successTest)
driver.close()