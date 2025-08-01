from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumObject:
    def __init__(self):
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() if using Firefox
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()