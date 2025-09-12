import pandas as pd
import numpy as np


#datas = pd.date_range('20250903', periods=30)

df = pd.DataFrame(np.random.randn (6,4), columns= ['Carros', 'Data', 'Pais', 'Região'])
print(df)

df2 = pd.DataFrame({"A": 7,
                    "B": pd.Timestamp('20250101'),
                    "C": pd.Series(1, index=list(range(4)),dtype='float32'),
                    "D": np.array([3]*4, dtype='int32'),
                    "E": pd.Categorical(['Teste', 'NaN', 'Teste', 'NaN']),
                     "F": 'Python' })

print(df2)