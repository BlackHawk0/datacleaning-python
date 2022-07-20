import pandas as pd
import numpy as np

df = pd.read_csv('Capstoneproject.csv')

# this will give us the info about the data
# df.info()

#remove null columns and rows
df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='any')

# checking for ideas
df["is_duplicate"] = df.duplicated()
print("\n {}".format(df))

# removing duplicates
DF_RM_DUP = df.drop_duplicates(keep='first')

# removing the is_duplicate column
DF_RM_DUP.pop('is_duplicate')

#save cleaned data to csv file
DF_RM_DUP.to_csv('Capstoneproject_cleaned.csv', index=False)
