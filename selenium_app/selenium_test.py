from time import sleep
import allure
import time
from selenium_app.playwrite_actions import RegisterPlaywrightActions
from selenium_app.selenium_actions import RegisterSeleniumActions

SITE_URL = "https://demoblaze.com/"


def register_a_user_playwright(playwright_driver, username, password):
    playwright_driver.goto(SITE_URL)
    playwright_register_actions = RegisterPlaywrightActions(playwright_driver)
    alert_message = playwright_register_actions.register_a_new_user(username, password)
    return alert_message


@allure.epic("Demo Epic")
@allure.feature("Demo Feature")
@allure.story("playwright tests")
@allure.tag("playwright")
@allure.title("create_new_account_with_existing_user_playwright")
def test_create_new_account_with_existing_user_playwright(playwright_driver):
    alert_message = register_a_user_playwright(playwright_driver, "hilit", "prizant")
    assert alert_message == "This user already exist."
   # slack.send_message("test_create_new_account_with_existing_user_playwright passed", "good")


@allure.epic("Demo Epic")
@allure.feature("Demo Feature")
@allure.story("playwright tests")
@allure.tag("playwright")
@allure.title("test_create_new_account_with_new_user_playwright")
def test_create_new_account_with_new_user_playwright(playwright_driver):
    user = "hilit" + str(int(time.time()))
    password = "prizant" + str(int(time.time()))
    alert_message = register_a_user_playwright(playwright_driver, user, password)
    assert alert_message == "Sign up successful."
#    slack.send_message("test_create_new_account_with_new_user_playwright passed", "good")


def register_a_user_selenium(selenium_driver, username, password):
    selenium_driver.get(SITE_URL)
    register_actions = RegisterSeleniumActions(selenium_driver)
    alert_message = register_actions.register_a_new_user(username, password)
    sleep(2)
    return alert_message


@allure.epic("Demo Epic")
@allure.feature("Demo Feature")
@allure.story("selenium tests")
@allure.tag("selenium")
@allure.title("test_create_new_account_with_existing_user_selenium")
def test_create_new_account_with_existing_user_selenium(selenium_driver):
    alert_message = register_a_user_selenium(selenium_driver,"hilit", "prizant")
    assert alert_message == "This user already exist."


@allure.epic("Demo Epic")
@allure.feature("Demo Feature")
@allure.story("selenium tests")
@allure.tag("selenium")
@allure.title("test_create_new_account_with_new_user_selenium")
def test_create_new_account_with_new_user_selenium(selenium_driver):
    user = "hilit" + str(int(time.time()))
    password = "prizant" + str(int(time.time()))
    alert_message = register_a_user_selenium(selenium_driver, user, password)
    assert alert_message == "Sign up successful."
#    slack.send_message("test_create_new_account_with_new_user_selenium passed", "good")
