import os

import pandas as pd

from selenium_app.slack_util import Slack

RESULTS_PATH = '/tmp/text_results.csv'
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\0330m]"
check = "\u2705"
cross = "\u274C"

def delete_results_file():
    if os.path.exists(RESULTS_PATH):
        os.remove(RESULTS_PATH)


def add_tests_results_to_report(test_name, outcome, duration):
    if outcome == 'passed':
        outcome = f"{check} Success"
    else:
        outcome = f"{cross} Failed"
    test_name = test_name.split('::')[-1]  # Get the last part of the test name
    df_current_test = pd.DataFrame(data={
        'Test Name': [test_name],
        'Outcome': [outcome],
        'Duration': [duration]
    })
    if os.path.exists(RESULTS_PATH):
        results_df = pd.read_csv(RESULTS_PATH)
        results_df = pd.concat([results_df, df_current_test], ignore_index=True)
    else:
        results_df = df_current_test
    results_df.to_csv(RESULTS_PATH, index=False)


def send_results_to_slack():
    df = pd.read_csv(RESULTS_PATH)
    slack = Slack()
    slack.send_slack_message_with_results_summery(df)