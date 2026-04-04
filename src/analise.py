import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar dados
# Certifique-se que o arquivo está na mesma pasta do script
df = pd.read_excel("../data/basealunosscoreevasao.xlsx")

# 2. Limpeza
# Remove números que possam estar misturados nos nomes dos alunos
df['nome'] = df['nome'].str.replace(r'\d+', '', regex=True)

# 3. Criar faixa de score
def definir_faixa(score):
    if score < 300:
        return 'Baixo'
    elif score <= 600:
        return 'Médio'
    else:
        return 'Alto'

df['faixa_score'] = df['score'].apply(definir_faixa)

# 4. Análise de evasão
# Calcula a média (taxa) de evasão por faixa
evasao_por_faixa = df.groupby('faixa_score')['evasao'].mean()
print("Taxa de Evasão por Faixa de Score:")
print(evasao_por_faixa)

# 5. Diferencial: Criar Score de Risco
df['risco'] = df['score'].apply(lambda x: 'Alto Risco' if x < 400 else 'Baixo Risco')

# 6. Visualização
evasao_por_faixa.plot(kind='bar', color=['red', 'yellow', 'green'])
plt.title('Taxa de Evasão por Faixa de Score')
plt.xlabel('Faixa de Pontuação')
plt.ylabel('Proporção de Evasão')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

