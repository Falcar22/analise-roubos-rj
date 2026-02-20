import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_clean/upp_rj_tratado.csv')

# filtrar só Vila Kennedy
vk = df[df['upp'] == 'Vila Kennedy']

serie_vk = vk.groupby('data')['total_roubos'].sum()

plt.figure(figsize=(12,5))
serie_vk.plot()
plt.title('Evolução de roubos - UPP Vila Kennedy')
plt.xlabel('Ano')
plt.ylabel('Total de roubos')
plt.tight_layout()

plt.savefig('vila_kennedy_serie.png', dpi=300)
plt.show()
