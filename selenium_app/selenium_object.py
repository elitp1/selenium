import os
import tempfile

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumObject:
    def __init__(self):
        user_data_dir = tempfile.mkdtemp(prefix="chrome_profile_", dir="/tmp")
        os.chmod(user_data_dir, 0o777)

        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")  # Required in many Docker environments
        options.add_argument("--disable-dev-shm-usage")  # Helps with shared memory issues
        options.add_argument("--disable-gpu")  # Just in case, especially in headless
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)  # or webdriver.Firefox() if using Firefox

    def navigate_to(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()