import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

print(df[df['Year'] > 1980][['Year','Track']])