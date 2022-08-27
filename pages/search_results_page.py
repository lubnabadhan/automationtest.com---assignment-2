from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SearchResultsPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )
    
    def get_search_results(self):
        self.wait.until(EC.title_is(("Search - My Store")))
        product_list = list(map(lambda product_title: product_title.text, 
                                self.driver.find_elements(By.XPATH, "//h5[@itemprop='name']/a")))
        return product_list