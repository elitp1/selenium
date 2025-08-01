import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class SeleniumActions:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    @allure.step("click_element_by_link_text")
    def click_element_by_link_text(self, link_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        element.click()

    @allure.step("click_element_by_name")
    def click_element_by_name(self, link_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, link_text)))
        element.click()

    @allure.step("fill_input_by_name")
    def fill_input_by_name(self, element, text_tol_fill):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, element)))
        element.send_keys(text_tol_fill)

    @allure.step("select_option_from_dropdown_by_name_and_value")
    def select_option_from_dropdown_by_name_and_value(self, element, value):
        dropdown = Select(self.driver.find_element(By.NAME, element))
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, element)))
        dropdown.select_by_value(value=value)

    @allure.step("select_option_from_radio_btn_by_name_and_value")
    def select_option_from_radio_btn_by_name_and_value(self, element, value):
        radio_btn_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.NAME, element)))
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
