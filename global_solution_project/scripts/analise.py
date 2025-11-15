
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/consumo.csv')
plt.plot(df['Hora'], df['Consumo_W'])
plt.xticks(rotation=45)
plt.title('Consumo de Energia')
plt.xlabel('Hora')
plt.ylabel('W')
plt.tight_layout()
plt.savefig('consumo_grafico.png')
