import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import Homepage
from pages.search_results_page import SearchResultsPage

@pytest.mark.usefixtures("setup")
class TestHomepage:
    def test_search_valid_query(self):
        expected_search_results = ["Printed Summer Dress", "Printed Dress", "Printed Chiffon Dress", 
                                   "Printed Summer Dress", "Printed Dress",]
        self.homepage = Homepage(self.driver, self.wait)
        self.search_results_page = SearchResultsPage(self.driver, self.wait)
        self.homepage.go_to_page("homepage")
        self.homepage.search_for_items("Printed")
        actual_search_results = self.search_results_page.get_search_results()
        assert actual_search_results == expected_search_results
        
    def test_quick_add_to_cart(self):
        expected_message = "Product successfully added to your shopping cart"
        self.homepage = Homepage(self.driver, self.wait)
        self.homepage.go_to_page("homepage")
        self.homepage.add_item_to_cart()
        self.wait.until(EC.visibility_of_element_located((By.ID, "layer_cart")))
        assert self.driver.find_element(By.XPATH, f"//h2[contains(.,  '{expected_message}')]")