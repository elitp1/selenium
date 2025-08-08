from time import sleep
import allure
import time
from playwrightobject import PlaywrightObject
from selenium_actions import SeleniumActions
from selenium_object import SeleniumObject


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("story level")
@allure.title("Test Create New Account on Facebook1")
@allure.tag("tag1")
def test_create_new_account1():
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


@allure.epic("epic level")
@allure.feature("feature level")
@allure.story("story level")
@allure.title("Test Create New Account on Facebook2")
@allure.tag("tag1")
def test_create_new_account2():
    with SeleniumObject() as selenium_obj:
        selenium_obj.navigate_to("https://www.facebook.com")
        selenium_actions = SeleniumActions(selenium_obj.driver)
        selenium_actions.click_element_by_link_text("Create new account")
        selenium_actions.fill_input_by_name("firstname", "Hilit")
        selenium_actions.fill_input_by_name("lastname", "prizant")
        selenium_actions.select_option_from_dropdown_by_name_and_value("birthday_month", "10")
        selenium_actions.select_option_from_dropdown_by_name_and_value("birthday_day", "3")
        selenium_actions.select_option_from_dropdown_by_name_and_value("birthday_year", "1973")
        selenium_actions.select_option_from_radio_btn_by_name_and_value("sex", "2")
        selenium_actions.fill_input_by_name("reg_email__", "elitp@walla.co.il")
        sleep(3)
        selenium_actions.click_element_by_name("websubmit")
        sleep(6)
        assert selenium_actions.wait_for_text_to_appear_in_element_type("div",
                                                                        "Enter a combination of at least six numbers")
