import pandas as pd
import numpy as np

series = pd.Series([2, 4, 7, np.nan, 10, 3])
print(series)
type(series)

datas = pd.date_range('20250903', periods=30)
print(datas)