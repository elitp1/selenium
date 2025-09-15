import tabulate
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
    channel = "#new-channel"

    def __init__(self):
        self.client = WebClient(token="")

    def send_slack_message_with_results_summery(self, df):
        try:
            table_text = tabulate.tabulate(df,headers='keys',tablefmt='simple',showindex=False)
            response = self.client.chat_postMessage(
                channel=Slack.channel,
                text="Test Results Summary",
                attachments=[
                    {
                        "color": "#1236b7",
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

    def send_slack_message(self, text, parent_thread=None):
        try:
            response = self.client.chat_postMessage(
                channel=Slack.channel,
                text=text,
                thread_ts=parent_thread
            )
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
            return None

    def send_slack_summery(self, df):
        response = self.send_slack_message_with_results_summery(df.loc[:, ['Test Name', 'Outcome', 'Duration']])
        if not response:
            return
        for _, row in df.iterrows():
            if "Success" not in row['Outcome']:
                self.send_slack_message(f"*Test Name*: {row['Test Name']}\n"
                                        f"*Outcome*: {row['Outcome']}\n"
                                        f"*Error*: {row['error']}",
                                        response["ts"])
