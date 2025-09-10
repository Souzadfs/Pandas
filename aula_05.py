import pandas as pd

df = pd.DataFrame({'A': ['A1', 'A2', 'A3', 'A4'],
                   'B': ['B1', 'B2', 'B3', 'B4',],
                   'C': ['C1', 'C2', 'C3', 'C4']},
                   index=[1, 2, 3, 4])

df1 = pd.DataFrame({'A': ['A5', 'A6', 'A7', 'A8'],
                    'B': ['B5', 'B6', 'B7', 'B8'],
                    'C': ['C5', 'C6', 'C7', 'C8']},
                    index= [1, 2, 3, 4])

#df2 = pd.DataFrame({'A': []})

frames= [df, df1]

concatenar = pd.concat(frames, keys=['f1', 'f2'])

print(concatenar)
print('---------------')
print(df)
print('---------------')
print(df1)