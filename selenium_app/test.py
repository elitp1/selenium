from threading import Thread, Lock
from time import sleep
import random
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})


def a(i,lock):
    number = random.randrange(0,100)
    sleep(number)
    with lock:
        print(i)


treads = []
lock = Lock()
for i in range(100):
    t = Thread(target=a, args=[i,lock])
    t.start()
    treads.append(t)
for item in treads:
    item.join()

