import pandas as pd

df1 = pd.read_csv('first-csv.csv')
df2 = pd.read_csv('first-csv.csv')

df3 = pd.merge(df1, df2, on = 'first-value-to-match')
df3.set_index('first-value-to-match', inplace = True)

df3.to_csv('merged-csv-documents.csv')