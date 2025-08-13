from enum import Enum
from threading import Thread, Lock
from time import sleep
import random
import pandas as pd
from pip._internal.utils.misc import enum

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})


class TESTING(Enum):
    A = "1"
    B = "2"
    C = "3"


for item in TESTING:
    print(item)


