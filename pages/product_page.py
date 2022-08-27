from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class ProductPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )

    def wait_for_product_added_modal_to_appear(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "layer_cart")))

    def add_item_to_cart_from_product_page(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))).click()
        
    def add_item_to_wishlist(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "wishlist_button"))).click()
        
    def increase_item_quantity(self, count):
        for i in range(count):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='icon-plus']"))).click()
            
    def select_item_size(self, size):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@id='group_1']//option[text()='{size}']"))).click()
        
    def select_item_color(self, color):
        self.wait.until(EC.element_to_be_clickable((By.NAME, color))).click()
        
    def product_attribute_seperator(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "layer_cart_product_attributes"))).text.split(", ")

