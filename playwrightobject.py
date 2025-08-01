import allure
from playwright.sync_api import sync_playwright


class PlaywrightObject:
    def __init__(self, url):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        self.p = p
        self.page = page
        self.browser = browser
        self.page.goto(url)
        self.page.set_viewport_size({"width": 1920, "height": 1080})

    @allure.step("Click button by text")
    def click_btn_by_txt(self, text):
        locator = self.page.get_by_text(text)
        locator.wait_for(state="visible")
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.page.close()
        self.browser.close()
        self.p.stop()