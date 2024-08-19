import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from e2e.features.sauceDemoFeature import SauceDemoFeature

class TestSauceDemoFeature(unittest.TestCase):
    def setUp(self):
        # This runs before each test method
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.sauce_demo_feature = SauceDemoFeature(self.driver)

        self.sauce_demo_feature.visit_sauce_demo_page()
        self.sauce_demo_feature.login()

    def tearDown(self):
        # This runs after each test method
        self.driver.quit()

    def test_1_home_page(self):
        self.sauce_demo_feature.assert_home_page()
        print("\nCheck home page test passed")

    def test_2_home_products_and_prices(self):
        self.sauce_demo_feature.check_home_products_and_prices()
        print("\nCheck home page products test passed")

    def test_3_add_to_cart_process(self):
        self.sauce_demo_feature.add_to_cart(1) # select a number between 1 and 6 due to the number of items in the inventory
        print("\nCheck add to cart process test passed")

    def test_4_ordering_item_process(self):
        self.sauce_demo_feature.check_ordering_item_process(2) # select a number between 1 and 6 due to the number of items in the inventory
        print("\nCheck ordering item process test passed")

if __name__ == "__main__":
    unittest.main()
