from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.homepage_locators import HomePageLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        self.type_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)

    def assert_error_message(self):
        self.find_element(LoginLocators.ALERT_CREDENTIAL)
