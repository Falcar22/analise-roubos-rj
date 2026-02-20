import pandas as pd

# ler dados
df = pd.read_csv('data_raw/UppEvolucaoMensalDeTitulos.csv', encoding='latin-1', sep=';')

# juntar ano + mês em uma data real
df['data'] = pd.to_datetime(df['ano'].astype(str) + '-' + df['mes'].astype(str) + '-01')

# ordenar cronologicamente
df = df.sort_values('data')

# verificar valores nulos
print("VALORES NULOS:")
print(df.isnull().sum())

# visualizar
print("\nPrimeiras datas:")
print(df[['upp','data','total_roubos','total_furtos']].head())

# salvar base tratada
df.to_csv('data_clean/upp_rj_tratado.csv', index=False)
