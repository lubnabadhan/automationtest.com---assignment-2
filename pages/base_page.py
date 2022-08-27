from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class BasePage():
        
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.__url_dict = {
        "homepage" : "http://automationpractice.com/index.php",
        "login_page" : "http://automationpractice.com/index.php?controller=authentication&back=my-account",
        "contact_us_page" : "http://automationpractice.com/index.php?controller=contact"
    }

    def go_to_page(self, page):
        self.driver.get(self.__url_dict[page])
        
    def mouse_hover_over_and_click_hidden_element(self, element, hidden_element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(hidden_element).perform()
        
    def choose_dropdown_option(self, element, dropdown_text):
        self.select = Select(element)
        self.select.select_by_visible_text(dropdown_text)