
#pytest -m smoke    //Tagging
#pytest -n 10  //pytest-xdist plugin you need to run in parallel

import json
import os.path
import sys

import pytest
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#-- Chromedriver
from selenium.webdriver.chrome.service import Service
#-- chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage

test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data= json.load(f)
    test_list= test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver= browserInstance

    loginPage = LoginPage(driver)
    loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    print(loginPage.getTitle())
    shopPage = ShopPage(driver)
    shopPage.add_product_to_cart(test_list_item["productName"])
    print(shopPage.getTitle())
    checkout_confirmation= shopPage.go_To_Cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()


    #  //a[contains(@href,'shop')]     a[href*='shop']---> CSS