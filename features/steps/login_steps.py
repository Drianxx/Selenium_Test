import json
import os
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('user is on login page')
def step_impl_given(context):
    # Membuka halaman login dan tunggu elemen muncul
    context.login_page.open()
    assert context.login_page.is_on_login_page(), "Tidak berada di halaman login"

@when('user login as "{user_type}"')
def step_impl(context, user_type):
    # 1. Tentukan path file JSON (relatif terhadap root project)
    file_path = os.path.join(os.getcwd(), 'data', 'accounts.json')
    
    # 2. Buka dan baca file JSON
    with open(file_path, 'r') as f:
        user_data = json.load(f)
    
    # 3. Ambil data berdasarkan user_type (misal: "standard_user")
    try:
        credentials = user_data[user_type]
    except KeyError:
        raise AssertionError(f"User type '{user_type}' not found in {file_path}")

    username = credentials['username']
    password = credentials['password']

    # 4. Lakukan login dengan kredensial yang diambil
    context.login_page.login(username, password)

@then('user should be redirected to dashboard')
def step_impl_then(context):
    # Tunggu sampai URL berisi inventory dan elemen dashboard tersedia
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains("inventory.html"))
    wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
    assert "inventory.html" in context.driver.current_url