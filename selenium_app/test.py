import pandas as pd


m = pd.DataFrame(data={'a': [1,2,3], 'b': [4,5,6]})

for row in m.iterrows():
    print(row[1]['b'])
