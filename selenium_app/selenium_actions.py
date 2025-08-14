from time import sleep

import allure
import selenium
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("click_element")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("fill_input")
    def fill_input(self, locator, text_to_fill):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text_to_fill)

    @allure.step("wait_for_alert")
    def wait_for_alert(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()  # Accept the alert
            return alert_text
        except TimeoutException:
            return False

    @allure.step("select_option_from_dropdown_by_name_and_value")
    def select_option_from_dropdown_by_name_and_value(self, element, value):
        dropdown = Select(self.driver.find_element(By.NAME, element))
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, element)))
        dropdown.select_by_value(value=value)

    @allure.step("select_option_from_radio_btn_by_name_and_value")
    def select_option_from_radio_btn_by_name_and_value(self, element, value):
        radio_btn_elements = self.wait.until(EC.presence_of_all_elements_located((By.NAME, element)))
        for radio_btn in radio_btn_elements:
            if radio_btn.get_attribute("value") == value:
                radio_btn.click()
                break

    @allure.step("wait_for_text_to_appear_in_element_type")
    def wait_for_text_to_appear_in_element_type(self, type, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//{type}[contains(.,'{text}')]")))
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


class RegisterSeleniumActions(SeleniumActions):
    def __init__(self, driver):
        super().__init__(driver)

    REGISTER_LINK = (By.LINK_TEXT, "Sign up")
    REGISTER_USERNAME_INPUT = (By.ID, "sign-username")
    REGISTER_PASSWORD_INPUT = (By.ID, "sign-password")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Sign up')]")

    @allure.step(f"register_a_new_user")
    def register_a_new_user(self, username, password):
        self.click_element(RegisterSeleniumActions.REGISTER_LINK)
        sleep(2)
        self.fill_input(RegisterSeleniumActions.REGISTER_USERNAME_INPUT, username)
        self.fill_input(RegisterSeleniumActions.REGISTER_PASSWORD_INPUT, password)
        self.click_element(RegisterSeleniumActions.REGISTER_BUTTON)
        sleep(2)
        alert_text = self.wait_for_alert()
        return alert_text

