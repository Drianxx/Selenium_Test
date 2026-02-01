from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import BASE_URL

class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(BASE_URL)
        # Tunggu sampai field username terlihat sebagai indikasi halaman login ready
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username, password):
        # Tunggu input terlihat dan tombol bisa diklik sebelum interaksi
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def is_on_login_page(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.USERNAME))
            return True
        except TimeoutException:
            # Jika timeout, fallback ke cek URL
            return "saucedemo" in self.driver.current_url
