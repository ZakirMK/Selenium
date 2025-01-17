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

    def find_elements(self, locator):
        """Waits until the elements are visible and return it."""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator):
        """Waits for the element to be clickable and clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Waits for an input field to be visible and types text into it."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def verify_text(self, locator, expected_text):
        """Verifies that the element's text matches the expected value."""
        element = self.find_element(locator)
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Expected '{expected_text}', but found '{actual_text}'"

    def verify_text_by_index(self, locator, index, expected_text):
        """Verifies that a specific item in a list of elements matches the expected text."""
        elements = self.find_elements(locator)
        assert index < len(elements), f"Index {index} is out of range. Found {len(elements)} elements."
        actual_text = elements[index].text.strip()
        assert actual_text == expected_text, f"Expected '{expected_text}', but found '{actual_text}'"