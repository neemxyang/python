import pandas as pd 
import openpyxl
from pandas import to_datetime
from datetime import datetime

df = pd.read_excel('d:\\gitdir\\2.xlsx', header=1)
df = pd.DataFrame(df)
print(df.dtypes)
df['日期'] = to_datetime(df.日期)
print(df.dtypes)
print(df.index)
df = df[['日期','借','贷']]

# print(df)

 