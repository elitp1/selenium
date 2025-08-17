from time import sleep
import allure
import time

from selenium_app.playwrightobject import PlaywrightObject
from selenium_app.playwrite_actions import RegisterPlaywrightActions
from selenium_app.selenium_actions import RegisterSeleniumActions
from selenium_app.selenium_object import SeleniumObject
from selenium_app.slack_util import Slack

SITE_URL = "https://demoblaze.com/"
slack = Slack()


def register_a_user_playwright(username, password):
    with PlaywrightObject() as playwright_obj:
        playwright_obj.navigate_to(SITE_URL)
        playwright_register_actions = RegisterPlaywrightActions(playwright_obj.page)
        alert_message = playwright_register_actions.register_a_new_user(username, password)
        return alert_message


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("playwright tests")
@allure.title("test_create_new_account_with_existing_user_playwright")
@allure.tag("playwright")
def test_create_new_account_with_existing_user_playwright():
    alert_message = register_a_user_playwright("hilit", "prizant")
    assert alert_message == "This user already exist."
   # slack.send_message("test_create_new_account_with_existing_user_playwright passed", "good")


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("playwright tests")
@allure.title("test_create_new_account_with_new_user_playwright")
@allure.tag("playwright")
def test_create_new_account_with_new_user_playwright():
    user = "hilit" + str(int(time.time()))
    password = "prizant" + str(int(time.time()))
    alert_message = register_a_user_playwright(user, password)
    assert alert_message == "Sign up successful."
#    slack.send_message("test_create_new_account_with_new_user_playwright passed", "good")


def register_a_user_selenium(username, password):
    with SeleniumObject() as selenium_obj:
        selenium_obj.navigate_to(SITE_URL)
        register_actions = RegisterSeleniumActions(selenium_obj.driver)
        alert_message = register_actions.register_a_new_user(username, password)
        sleep(2)
        return alert_message


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("selenium tests")
@allure.title("test_create_new_account_with_existing_user_selenium")
@allure.tag("selenium")
def test_create_new_account_with_existing_user_selenium():
    alert_message = register_a_user_selenium("hilit", "prizant")
    assert alert_message == "Thiss user already exist."
    # slack.send_message(f"test_create_new_account_with_existing_user_selenium {result}", color)


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("selenium tests")
@allure.title("test_create_new_account_with_new_user_selenium")
@allure.tag("selenium")
def test_create_new_account_with_new_user_selenium():
    user = "hilit" + str(int(time.time()))
    password = "prizant" + str(int(time.time()))
    alert_message = register_a_user_selenium(user, password)
    assert alert_message == "Sign up successful."
#    slack.send_message("test_create_new_account_with_new_user_selenium passed", "good")
