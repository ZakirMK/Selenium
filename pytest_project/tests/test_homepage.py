import pytest
from selenium import webdriver
from pages.home_page import HomePage
from utils.helper import login
from config import Globals

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Globals.BASE_URL)
    login(driver)  # Call the login helper function
    yield driver
    driver.quit()

def test_verify_headers(driver):
    home_page = HomePage(driver)
    home_page.assert_dashboard_exists()
    home_page.assert_upgrade_exists()
    home_page.assert_profile_exists()

def test_verify_homepage_menu_items(driver):
    home_page = HomePage(driver)
    home_page.assert_menu_items(0, Globals.MENU_ITEM_TEXT[0])    # Admin
    home_page.assert_menu_items(1, Globals.MENU_ITEM_TEXT[1])    # PIM
    home_page.assert_menu_items(2, Globals.MENU_ITEM_TEXT[2])    # Leave
    home_page.assert_menu_items(3, Globals.MENU_ITEM_TEXT[3])    # Time
    home_page.assert_menu_items(4, Globals.MENU_ITEM_TEXT[4])    # Recruitment
    home_page.assert_menu_items(5, Globals.MENU_ITEM_TEXT[5])    # My Info
    home_page.assert_menu_items(6, Globals.MENU_ITEM_TEXT[6])    # Performance
    home_page.assert_menu_items(7, Globals.MENU_ITEM_TEXT[7])    # Dashboard
    home_page.assert_menu_items(8, Globals.MENU_ITEM_TEXT[8])    # Directory
    home_page.assert_menu_items(9, Globals.MENU_ITEM_TEXT[9])    # Maintance
    home_page.assert_menu_items(10, Globals.MENU_ITEM_TEXT[10])  # Claim
    home_page.assert_menu_items(11, Globals.MENU_ITEM_TEXT[11])  # Buzz





