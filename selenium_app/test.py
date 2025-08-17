import datetime
from collections import Counter
from datetime import time

import pandas as pd
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from selenium_app.utils import add_tests_results_to_report, send_results_to_slack

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

send_results_to_slack()