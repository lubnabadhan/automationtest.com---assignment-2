from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )
        
    def go_to_login_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        
    def enter_login_and_sign_in(self, email, passwd):
        self.wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(email)
        self.driver.find_element(By.ID, "passwd").send_keys(passwd)
        self.driver.find_element(By.ID, "SubmitLogin").click()
        
    def click_forgot_your_password_link(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgot your password?"))).click()
        
    def enter_account_creation_email_and_continue(self, email):
        self.wait.until(EC.element_to_be_clickable((By.ID, "email_create"))).send_keys(email)
        self.driver.find_element(By.ID, "SubmitCreate").click()

    def quick_valid_login(self):
        self.go_to_login_page()
        self.enter_login_and_sign_in("lubnabadhan178@gmail.com", "ruhul@1234")
        