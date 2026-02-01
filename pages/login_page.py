from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import BASE_URL
from locators.login_locators import Loginlocators

class LoginPage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.locators = Loginlocators

    def open(self):
        self.driver.get(BASE_URL)
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.USERNAME))
        except TimeoutException:
            raise AssertionError("Login page did not load or USERNAME element not found")

    def is_on_login_page(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.USERNAME))
            return True
        except TimeoutException:
            return "saucedemo" in self.driver.current_url

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.locators.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.locators.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.locators.LOGIN_BTN)).click()
