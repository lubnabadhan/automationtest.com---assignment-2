from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class Homepage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )
    
    def search_for_items(self, search_query):
        self.wait.until(EC.element_to_be_clickable((By.ID, "search_query_top"))).send_keys(search_query)
        self.driver.find_element(By.NAME, "submit_search").click()
        
    def add_item_to_cart(self):
        self.wait.until(EC.title_is(("My Store")))
        element = self.driver.find_element(By.XPATH, "//ul[@id='homefeatured']/li[1]")
        hidden_element = self.driver.find_element(By.XPATH, "//ul[@id='homefeatured']/li[1]//a[@title='Add to cart']")
        self.mouse_hover_over_and_click_hidden_element(element, hidden_element)

    def expand_item(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul/li[1]//a[@class='product_img_link']"))).click()