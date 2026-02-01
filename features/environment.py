from utils.driver_factory import create_driver
from pages.login_page import LoginPage

def before_scenario(context, scenario):
    context.driver = create_driver()
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()