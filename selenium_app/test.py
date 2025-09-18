from os import environ

import pandas as pd


print(environ.get('SLACK_TOKEN',None))