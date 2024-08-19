from code.sauceDemo.sauceDemo import SauceDemo

class SauceDemoFeature:
    def __init__(self, driver):
        self.sauce_demo = SauceDemo(driver)

    def visit_sauce_demo_page(self):
        self.sauce_demo.visit_sauce_demo()

    def login(self):
        self.sauce_demo.login()

    def assert_home_page(self):
        self.sauce_demo.assert_home_page()

    def check_home_products_and_prices(self):
        self.sauce_demo.check_home_products_and_prices()

    def cart_is_empty(self):
        self.sauce_demo.cart_is_empty()

    def add_to_cart(self, item_index):
        self.sauce_demo.add_to_cart(item_index)

    def assert_item_is_added_to_cart(self, item_index):
        self.sauce_demo.assert_item_is_added_to_cart(item_index)

    def check_add_to_cart_process(self, item_index):
        self.cart_is_empty()
        self.add_to_cart(item_index)
        self.assert_item_is_added_to_cart(item_index)

    def click_checkout(self):
        self.sauce_demo.click_checkout()

    def fill_address_form(self):
        self.sauce_demo.fill_address_form()

    def click_continue(self):
        self.sauce_demo.click_continue()

    def assert_checkout_review(self):
        self.sauce_demo.assert_checkout_review()

    def click_finish(self):
        self.sauce_demo.click_finish()

    def assert_order_complete(self):
        self.sauce_demo.assert_order_complete()

    def check_ordering_item_process(self, item_index):
        self.check_add_to_cart_process(item_index)
        self.click_checkout()
        self.fill_address_form()
        self.click_continue()
        self.assert_checkout_review()
        self.click_finish()
        self.assert_order_complete()
