import pandas as pd

# carregar base tratada
df = pd.read_csv('data_clean/upp_rj_tratado.csv')

# total de roubos por ano
roubos_por_ano = df.groupby('ano')['total_roubos'].sum()
print("\nROUBOS POR ANO:")
print(roubos_por_ano)

# total de furtos por ano
furtos_por_ano = df.groupby('ano')['total_furtos'].sum()
print("\nFURTOS POR ANO:")
print(furtos_por_ano)

# UPPs com mais roubos
top_upps = df.groupby('upp')['total_roubos'].sum().sort_values(ascending=False).head(10)
print("\nTOP 10 UPPs COM MAIS ROUBOS:")
print(top_upps)

import matplotlib.pyplot as plt

# somar roubos por mês
serie_temporal = df.groupby('data')['total_roubos'].sum()

plt.figure(figsize=(12,5))
serie_temporal.plot()
plt.title('Evolução mensal de roubos no RJ (UPPs)')
plt.xlabel('Ano')
plt.ylabel('Total de roubos')
plt.tight_layout()
plt.savefig('grafico_roubos_rj.png', dpi=300)
plt.show()

