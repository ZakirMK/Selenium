from pages.login_page import LoginPage
from config import Globals

def login(driver):
    """Helper function to log in."""
    login_page = LoginPage(driver)
    login_page.enter_username(Globals.VALID_USERNAME)
    login_page.enter_password(Globals.VALID_PASSWORD)
    login_page.click_login()
