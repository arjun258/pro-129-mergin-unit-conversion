import pandas as pd
df = pd.read_csv('dwarf_stars.csv')
df = df.dropna()
df["UnitsRadius"] = 0.102763*df["UnitsRadius"]
df.dtypes
print(df)
df.dtypes
df["UnitsMass"] = df.UnitsMass.astype(float)
df.dtypes
df['UnitsMass'] = df['UnitsMass']*0.000954588 
print(df['UnitsMass'])

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.columns

df.reset_index(drop=True,inplace=True)
df.to_csv('unitConverted.csv')