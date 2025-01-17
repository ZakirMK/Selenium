import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config import Globals

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Globals.BASE_URL)
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.enter_username(Globals.VALID_USERNAME)
    login_page.enter_password(Globals.VALID_PASSWORD)
    login_page.click_login()
    home_page.assert_dashboard_exists()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    
    login_page.enter_username(Globals.VALID_USERNAME)
    login_page.enter_password(Globals.INVALID_PASSWORD)
    login_page.click_login()
    login_page.assert_error_message()

