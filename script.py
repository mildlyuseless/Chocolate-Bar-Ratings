import pandas as pd
# import seaborn as sns

df = pd.read_csv('data/chocolate_bars.csv')
print(df.head())

print(df.describe())

print(df.info())

beans = df.groupby('bean_origin')['rating'].mean()
print(beans)


