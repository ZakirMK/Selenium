from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
    ALERT_CREDENTIAL = (By.CSS_SELECTOR, '[role="alert"]')