import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_unsuccessfully(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.go_to_page("login_page")
        self.login_page.enter_login_and_sign_in("lubnabadhan178@gmail.com", "ruhul@12341")
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div/p[text() = 'There is 1 error']")))

    def test_login_successfully(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.go_to_page("login_page")
        self.login_page.enter_login_and_sign_in("lubnabadhan178@gmail.com", "ruhul@1234")
        assert self.wait.until(EC.visibility_of_element_located((By.ID, "my-account")))
        
    def test_forgot_password_redirect(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.go_to_page("login_page")
        self.login_page.click_forgot_your_password_link()
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text() = 'Forgot your password?']")))
        
    def test_unsuccessful_account_creation_bad_email(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.go_to_page("login_page")
        self.login_page.enter_account_creation_email_and_continue("")
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text() = 'Invalid email address.']")))
        
    def test_unsuccessful_account_creation_dupe_email(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.go_to_page("login_page")
        self.login_page.enter_account_creation_email_and_continue("lubnabadhan178@gmail.com")
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'email address has already been registered')]")))