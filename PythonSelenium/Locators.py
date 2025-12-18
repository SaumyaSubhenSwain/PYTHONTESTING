import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver service Selenium 160-> 160 chrome driver
service_obj=Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# ID , Xpath, CSS Selector, name, Classname, Linktext
driver.find_element(By.NAME,"email").send_keys("helloworld@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH--> //tagname[@attributrvalue = 'value']   -> //input[@type='submit']
#CSS --> tagname[attributevalue = 'value']  --> input[type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Saumya")
# driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()
employed_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='option1']")
employed_radio.click()

#Static dropdown
dropDown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")
# dropDown.select_by_value()


driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert  "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(3)