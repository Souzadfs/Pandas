import pandas as pd
import numpy as np


#datas = pd.date_range('20250903', periods=30)

df = pd.DataFrame(np.random.randn (6,4), columns= ['Carros', 'Data', 'Pais', 'Região'])
print(df)