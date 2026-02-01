from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('user is on login page')
def step_impl_given(context):
    # Membuka halaman login dan tunggu elemen muncul
    context.login_page.open()
    assert context.login_page.is_on_login_page(), "Tidak berada di halaman login"

@when('user login with valid username and password')
def step_impl_when(context):
    # Memasukkan username dan password (sesuaikan dengan data Saucedemo)
    context.login_page.login("standard_user", "secret_sauce")

@then('user should be redirected to dashboard')
def step_impl_then(context):
    # Tunggu sampai URL berisi inventory dan elemen dashboard tersedia
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains("inventory.html"))
    wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
    assert "inventory.html" in context.driver.current_url