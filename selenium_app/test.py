import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df.loc[0:1, 'C'] = 999dfdf
print(df)