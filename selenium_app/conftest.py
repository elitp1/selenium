import os
import tempfile

import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver

from selenium_app.utils import add_tests_results_to_report, delete_results_file, send_results_to_slack


def pytest_sessionstart(session):
    delete_results_file()


def pytest_sessionfinish(session, exitstatus):
    send_results_to_slack()


def pytest_runtest_setup(item):
    pass


def pytest_runtest_teardown(item):
    pass


def pytest_runtest_logreport(report):
    if report.when == 'call':
        add_tests_results_to_report(report.nodeid,report.outcome, report.duration, report.longrepr)


@pytest.fixture()
def selenium_driver():
    user_data_dir = tempfile.mkdtemp(prefix="chrome_profile_", dir="/tmp")
    os.chmod(user_data_dir, 0o777)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")  # Required in many Docker environments
    options.add_argument("--disable-dev-shm-usage")  # Helps with shared memory issues
    options.add_argument("--disable-gpu")  # Just in case, especially in headless
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)  # or webdriver.Firefox() if using Firefox
    yield driver
    driver.quit()


@pytest.fixture()
def playwright_driver():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(locale="en-US")
    page = context.new_page()
    p = p
    page = page
    browser = browser
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()
    browser.close()
    p.stop()






