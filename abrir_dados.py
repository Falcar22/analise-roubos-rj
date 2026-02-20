import pandas as pd

df = pd.read_csv('data_raw/UppEvolucaoMensalDeTitulos.csv', encoding='latin-1', sep=';')

print(df.head())
print("\nCOLUNAS:")
print(df.columns)
print("\nLINHAS E COLUNAS:")
print(df.shape)
