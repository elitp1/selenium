import tabulate
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
    channel = "#new-channel"

    def __init__(self):
        self.client = WebClient(token="")

    def send_slack_message_with_results_summery(self, df):
        try:
            table_text = tabulate.tabulate(df,headers='keys',tablefmt='git')
            response = self.client.chat_postMessage(
                channel=Slack.channel,
                text="Test Results Summary",
                attachments=[
                    {
                        "color": "#36a64f",
                        "text": "current test results:",
                        "fields": [
                            {
                                "value": f"``` {table_text}```",
                                "short": False
                            }
                        ]
                    }
                ]
            )
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
            return None

    def send_slack_message(self, text):
        try:
            response = self.client.chat_postMessage(
                channel=Slack.channel,
                text=text
            )
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
            return None
