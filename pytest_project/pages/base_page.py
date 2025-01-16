from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        """Waits until the element is visible and returns it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Waits for the element to be clickable and clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Waits for an input field to be visible and types text into it."""
        element = self.find_element(locator)
        element.clear()  # Clear the field before typing
        element.send_keys(text)
