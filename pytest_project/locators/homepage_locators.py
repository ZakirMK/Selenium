from selenium.webdriver.common.by import By

class HomePageLocators:
    DASHBOARD = (By.CSS_SELECTOR, '[class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
    MENU_ITEMS = (By.CSS_SELECTOR, '[class="oxd-text oxd-text--span oxd-main-menu-item--name"]')
    UPGRADE_BUTTON = (By.CSS_SELECTOR, '[class="oxd-glass-button orangehrm-upgrade-button"]')
    PROFILE_BUTTON = (By.CSS_SELECTOR, '[class="oxd-userdropdown-tab"]')