from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from code.utils.credentials import credentials
from code.utils.sauceUsers import sauce_users
from code.utils.selectors import selectors

class SauceDemo:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.driver.maximize_window()
        self.element_number = 0

    def visit_sauce_demo(self):
        self.driver.get(credentials["sauce_demo_url"])

    def login(self):
        username_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["username"])))
        password_element = self.driver.find_element(By.CSS_SELECTOR, selectors["password"])
        login_button_element = self.driver.find_element(By.CSS_SELECTOR, selectors["login_button"])

        username_element.send_keys(sauce_users["standard_user"]["username"])
        password_element.send_keys(sauce_users["standard_user"]["password"])
        login_button_element.click()

    def assert_home_page(self):
        title_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["title"])))
        assert credentials["sauce_demo_title"] in title_element.text

    def assert_items_and_prices_got_same_length(self):
        if len(credentials["sauce_inventory_items"]) != len(credentials["sauce_inventory_items_prices"]):
            raise ValueError("Inventory items and prices arrays must be the same length")

    def check_home_products_and_prices(self):
        self.assert_items_and_prices_got_same_length()
        for index, inventory_item in enumerate(credentials["sauce_inventory_items"]):
            inventory_item_price = credentials["sauce_inventory_items_prices"][index]

            item_elements = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selectors["inventory_item"])))
            price_elements = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selectors["inventory_item_price"])))

            item_element = item_elements[index]
            price_element = price_elements[index]

            item_text = item_element.text
            price_text = price_element.text

            assert inventory_item in item_text, f"Expected item '{inventory_item}' not found in '{item_text}'."
            assert inventory_item_price in price_text, f"Expected price '{inventory_item_price}' not found in '{price_text}'."

    def cart_is_empty(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, selectors["shop_card_badge"])
            raise AssertionError("Cart is not empty")
        except:
            pass

    def set_element_number(self, item_index):
        self.element_number = item_index - 1

    def add_to_cart(self, item_index):
        self.set_element_number(item_index)
        add_to_cart_buttons = self.driver.find_elements(By.CSS_SELECTOR, selectors["add_to_cart_button"])
        add_to_cart_button = add_to_cart_buttons[self.element_number]
        add_to_cart_button.click()

    def assert_item_is_added_to_cart(self, item_index):
        self.set_element_number(item_index)

        remove_cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["remove_cart_button"])))
        assert remove_cart_button.is_displayed()

        shop_card_badge = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["shop_card_badge"])))
        assert '1' in shop_card_badge.text

        shopping_card = self.driver.find_element(By.CSS_SELECTOR, selectors["shopping_card"])
        shopping_card.click()
        
        item_name = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["inventory_name"])))
        assert credentials["sauce_inventory_items"][self.element_number] in item_name.text

        item_price = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["inventory_item_price"])))
        assert credentials["sauce_inventory_items_prices"][self.element_number] in item_price.text

    def click_checkout(self):
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, selectors["checkout_button"])
        checkout_button.click()

    def fill_address_form(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, selectors["first_name"])
        last_name = self.driver.find_element(By.CSS_SELECTOR, selectors["last_name"])
        zip_code = self.driver.find_element(By.CSS_SELECTOR, selectors["zip_code"])

        first_name.send_keys(credentials["sauce_first_name"])
        last_name.send_keys(credentials["sauce_last_name"])
        zip_code.send_keys(credentials["sauce_zip_code"])

    def click_continue(self):
        continue_button = self.driver.find_element(By.CSS_SELECTOR, selectors["continue_button"])
        continue_button.click()

    def assert_checkout_review(self):
        title_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["title"])))
        assert credentials["sauce_checkout_title"] in title_element.text

        item_name = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["inventory_name"])))
        item_price = self.driver.find_element(By.CSS_SELECTOR, selectors["inventory_item_price"])

        assert credentials["sauce_inventory_items"][self.element_number] in item_name.text
        assert credentials["sauce_inventory_items_prices"][self.element_number] in item_price.text

        summary_info = self.driver.find_element(By.CSS_SELECTOR, selectors["summary_info"])

        assert credentials["sauce_card"] in summary_info.text
        assert credentials["sauce_shipping_info"] in summary_info.text
        assert credentials['sauce_total_price'] in summary_info.text, f"Expected total price '{credentials['sauce_total_price']}' not found in summary info text. Found text: '{summary_info.text}'"

    def click_finish(self):
        finish_button = self.driver.find_element(By.CSS_SELECTOR, selectors["finish_button"])
        finish_button.click()

    def assert_order_complete(self):
        complete_header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["complete_header"])))
        assert credentials["sauce_checkout_complete_title"] in complete_header.text
