from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestSample:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print('Test completed.')

    def test_login(self, test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com')
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        driver.find_element(By.CSS_SELECTOR, '[class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
        driver.find_element(By.CSS_SELECTOR, '[class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')

# File name :  test_*.py or *_test.py
# Class name should start with Test