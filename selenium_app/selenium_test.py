from time import sleep
import allure
import time
from playwrightobject import PlaywrightObject
from selenium_actions import SeleniumActions, LoginSeleniumActions
from selenium_object import SeleniumObject


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("story level")
@allure.title("Test Create New Account on Facebook1")
@allure.tag("tag1")
def ytest_create_new_account1():
    with PlaywrightObject("https://facebook.com") as playwrite_obj:
        playwrite_obj.click_btn_by_txt("Create new account")
        playwrite_obj.fill_input_by_name("firstname", "Hilit")
        playwrite_obj.fill_input_by_name("lastname", "prizant")
        playwrite_obj.select_option_from_drop_down_by_name("birthday_month", "Oct")
        playwrite_obj.select_option_from_drop_down_by_name("birthday_day", "3")
        playwrite_obj.select_option_from_drop_down_by_name("birthday_year", "1973")
        playwrite_obj.select_option_from_radio_btn_by_value("sex", "2")
        playwrite_obj.fill_input_by_name("reg_email__", "elitp@walla.co.il")
        print(f'the last name is {playwrite_obj.get_value_of_element_by_name("lastname")}')
        playwrite_obj.click_btn_by_name("websubmit")
        time.sleep(3)
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
