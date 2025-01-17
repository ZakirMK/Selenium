from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators

class HomePage(BasePage):
    def assert_dashboard_exists(self):
        self.find_element(HomePageLocators.DASHBOARD)

    def assert_upgrade_exists(self):
        self.find_element(HomePageLocators.UPGRADE_BUTTON)

    def assert_profile_exists(self):
        self.find_element(HomePageLocators.PROFILE_BUTTON)

    def assert_menu_items(self, index, text):
        self.verify_text_by_index(HomePageLocators.MENU_ITEMS, index, text)