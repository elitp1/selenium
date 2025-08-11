from time import sleep
import allure
import time
from playwrightobject import PlaywrightObject
from selenium_actions import SeleniumActions, LoginSeleniumActions
from selenium_app.playwrite_actions import PlaywrightActions
from selenium_object import SeleniumObject


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("story level")
@allure.title("Test Create New Account on Facebook1")
@allure.tag("tag1")
def test_create_new_account1():
    with PlaywrightObject() as playwright_obj:
        playwright_obj.navigate_to("https://www.facebook.com/")
        playwright_actions = PlaywrightActions(playwright_obj.page)
        playwright_actions.click_btn_by_txt("Create new account")
        playwright_actions.fill_input_by_name("firstname", "Hilit")
        playwright_actions.fill_input_by_name("lastname", "prizant")
        playwright_actions.select_option_from_drop_down_by_name("birthday_month", "Oct")
        playwright_actions.select_option_from_drop_down_by_name("birthday_day", "3")
        playwright_actions.select_option_from_drop_down_by_name("birthday_year", "1973")
        playwright_actions.select_option_from_radio_btn_by_value("sex", "2")
        playwright_actions.fill_input_by_name("reg_email__", "elitp@walla.co.il")
        playwright_actions.click_btn_by_name("websubmit")
        time.sleep(10)
        assert True


def register_a_user(username, password):
    with SeleniumObject() as selenium_obj:
        selenium_obj.navigate_to("https://demoblaze.com/")
        login_actions = LoginSeleniumActions(selenium_obj.driver)
        alert_message = login_actions.register_a_new_user(username, password)
        sleep(2)
        return alert_message


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("story level")
@allure.title("Test Create New Account with_existing_user")
@allure.tag("tag1")
def test_create_new_account_with_existing_user():
    alert_message = register_a_user("hilit", "prizant")
    assert alert_message == "This user already exist."


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("story level")
@allure.title("Test Create New Account with new user")
@allure.tag("tag1")
def test_create_new_account_with_new_user():
    user = "hilit" + str(int(time.time()))
    password = "prizant" + str(int(time.time()))
    alert_message = register_a_user(user, password)
    assert alert_message == "Sign up successful."
