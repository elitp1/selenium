from selenium_app.selenium_test import slack
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
        add_tests_results_to_report(report.nodeid,report.outcome, report.duration)


