import pandas as pd
import numpy as np
print('Reading `submitted.csv` and converting to pandas dataframe')
df = pd.read_csv('submitted.csv')
df.fillna(0, inplace=True)
df['Battery' ] = df['Battery'].str.replace('%','').astype(float)
df['CT'] = df['CT'].str.replace(' seconds','').astype(float).fillna(0.0).astype(int)
df['DT'] = df['DT'].str.replace(' seconds','').astype(float).fillna(0.0).astype(int)
df['Datetime'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%dT%H:%M:%S%z')
print(df.head())
df.to_json('submitted.json', orient='records')
