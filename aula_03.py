import pandas as pd
import numpy as np

datas = pd.date_range('20250908', periods= 60, freq= "D")
df = pd.DataFrame(np.random.randn(60,5), index= datas, columns= list("ABCD"))

print(df, datas)
