import allure
from playwright.sync_api import sync_playwright


class PlaywrightObject:
    def __init__(self):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(locale="en-US")
        page = context.new_page()
        self.p = p
        self.page = page
        self.browser = browser
        self.page.set_viewport_size({"width": 1920, "height": 1080})

    def navigate_to(self, url):
        self.page.goto(url)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.page.close()
        self.browser.close()
        self.p.stop()