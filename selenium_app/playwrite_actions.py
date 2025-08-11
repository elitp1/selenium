import allure


class PlaywrightActions:
    def __init__(self, driver):
        self.page = driver

    @allure.step("Click button by text")
    def click_btn_by_txt(self, text):
        self.page.screenshot(path="/tmp/allure/before_click.png")
        locator = self.page.get_by_text(text)
        locator.wait_for(state="attached")
        locator.click()

    @allure.step("Click button by name")
    def click_btn_by_name(self, name):
        locator = self.page.locator(f'[name="{name}"]')
        locator.wait_for(state="visible")
        locator.click()

    @allure.step("fill input by name")
    def fill_input_by_name(self, element_name, text_to_fill):
        locator = self.page.locator(f'[name="{element_name}"]')
        locator.wait_for(state="visible")
        locator.fill(text_to_fill)

    @allure.step("select_option_from_drop_down_by_name")
    def select_option_from_drop_down_by_name(self, element_name, option_text):
        locator = self.page.locator(f'[name="{element_name}"]')
        locator.wait_for(state="visible")
        locator.select_option(label=option_text)

    @allure.step("select_option_from_radio_btn_by_value")
    def select_option_from_radio_btn_by_value(self, element_name, value):
        locator = self.page.locator(f'[name="{element_name}"][value="{value}"]')
        locator.wait_for(state="visible")
        locator.check()

    @allure.step("get_value_of_element_by_name")
    def get_value_of_element_by_name(self, element_name):
        locator = self.page.locator(f'[name="{element_name}"]')
        locator.wait_for(state="visible")
        return locator.input_value()