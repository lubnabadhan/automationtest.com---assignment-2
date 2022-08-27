from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class ContactUsPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )
    
    def fill_in_contact_us_form_and_send(self, subject_handling, email, order_reference, attach_file, message):
        self.wait.until(EC.visibility_of_element_located((By.ID, "uniform-id_contact")))
        subject_handling_element = self.driver.find_element(By.ID, "id_contact")
        if subject_handling:
            self.choose_dropdown_option(subject_handling_element, subject_handling)
        if email:
            self.driver.find_element(By.ID, "email").send_keys(email)
        if order_reference:
            self.driver.find_element(By.ID, "id_order").send_keys(order_reference)
        if attach_file:
            self.driver.find_element(By.ID, "fileUpload").send_keys(attach_file)
        if message:
            self.driver.find_element(By.ID, "message").send_keys(message)
        self.driver.find_element(By.ID, "submitMessage").click()