from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
    driver.implicitly_wait(4)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()

    # Click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']")

    # collect all  veggie names --> BrowserSortedveggieList  (B,A,C)
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in veggieWebElements:
        browserSortedVeggies.append(ele.text)
        # print(ele.text)

    originalBrowserSortedList = browserSortedVeggies.copy()