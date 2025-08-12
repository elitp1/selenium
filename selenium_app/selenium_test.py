from time import sleep
import allure
import time

from selenium_app.playwrightobject import PlaywrightObject
from selenium_app.playwrite_actions import LoginPlaywrightActions
from selenium_app.selenium_actions import LoginSeleniumActions
from selenium_app.selenium_object import SeleniumObject


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("playwright tests")
@allure.title("test_create_new_account_with_existing_user_playwright")
@allure.tag("tag1")
def test_create_new_account_with_existing_user_playwright():
    with PlaywrightObject() as playwright_obj:
        playwright_obj.navigate_to("https://demoblaze.com/")
        playwright_login_actions = LoginPlaywrightActions(playwright_obj.page)
        alert_message = playwright_login_actions.register_a_new_user("hilit", "prizant")
        sleep(2)
        print(alert_message)


def register_a_user(username, password):
    with SeleniumObject() as selenium_obj:
        selenium_obj.navigate_to("https://demoblaze.com/")
        login_actions = LoginSeleniumActions(selenium_obj.driver)
        alert_message = login_actions.register_a_new_user(username, password)
        sleep(2)
        return alert_message


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("selenium tests")
@allure.title("test_create_new_account_with_existing_user")
@allure.tag("tag1")
def test_create_new_account_with_existing_user():
    alert_message = register_a_user("hilit", "prizant")
    assert alert_message == "This user already exist."


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("selenium tests")
@allure.title("test_create_new_account_with_new_user_selenium")
@allure.tag("tag1")
def test_create_new_account_with_new_user_selenium():
    user = "hilit" + str(int(time.time()))
    password = "prizant" + str(int(time.time()))
    alert_message = register_a_user(user, password)
    assert alert_message == "Sign up successful."
