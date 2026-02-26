import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

print("Primeiras linhas")
print(df.head())
print("Ultimas linhas")
print(df.tail())