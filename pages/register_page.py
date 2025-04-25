import time

from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator_gender = (By.ID, "gender-female")
        self.locator_firstname = (By.NAME, "FirstName")
        self.locator_lastname = (By.NAME, "LastName")
        self.locator_email = (By.NAME, "Email")
        self.locator_password = (By.NAME, "Password")
        self.locator_confirm_password = (By.NAME, "ConfirmPassword")
        self.locator_register = (By.ID, "register-button")
        self.locator_expected_msg = (By.XPATH, "//div[@class='result']")

    def navigate_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)


    def register(self, firstname, lastname, email, password):
        self.driver.find_element(*self.locator_gender).click()
        self.driver.find_element(*self.locator_firstname).send_keys(firstname)
        self.driver.find_element(*self.locator_lastname).send_keys(lastname)
        self.driver.find_element(*self.locator_email).send_keys(email)
        self.driver.find_element(*self.locator_password).send_keys(password)
        self.driver.find_element(*self.locator_confirm_password).send_keys(password)
        self.driver.find_element(*self.locator_register).click()

    def expected_msg(self):
        expected_success_msg = self.driver.find_element(By.XPATH, "//div[@class='result']").text
        assert "Your registration completed".strip() in expected_success_msg.strip()


    def close_browser(self):
        self.driver.close()