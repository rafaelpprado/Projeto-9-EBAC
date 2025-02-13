# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo dos gráficos
sns.set(style="whitegrid")

# 1) Carregando a Base de Dados
print("Carregando os dados...")
df = pd.read_csv(r'C:\Users\ReReu\Downloads\python\Nova pasta\1\projeto8.csv', sep=';')

# Exibir as primeiras linhas do dataframe para conferir se os dados foram carregados corretamente
print("\nVisualizando as primeiras linhas:")
print(df.head())

# 2A) Estatísticas Descritivas
print("\nEstatísticas Descritivas:")
print(df.describe(include='all'))

# 2B) Identificação de possíveis outliers
print("\nIdentificando possíveis outliers...")
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot de {col}")
    plt.xlabel(col)
    plt.show()

# 2C) Análise Univariada - Gráficos para entender os dados
# Renomear coluna "Tempo_como_Cliente" caso necessário
if "Tempo_como_Cliente" in df.columns:
    df = df.rename(columns={"Tempo_como_Cliente": "Tempo_de_Cliente"})

# Gráfico 1: Distribuição de Tempo_de_Cliente por Churn
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='Tempo_de_Cliente', hue='Churn', bins=30, kde=True)
plt.title("Distribuição de Tempo_de_Cliente por Churn")
plt.xlabel("Tempo de Cliente (meses)")
plt.ylabel("Frequência")
plt.show()

# Gráfico 2: Boxplot do Pagamento Mensal por Churn
plt.figure(figsize=(8, 4))
sns.boxplot(x='Churn', y='Pagamento_Mensal', data=df)
plt.title("Pagamento Mensal por Churn")
plt.xlabel("Churn")
plt.ylabel("Pagamento Mensal")
plt.show()

# Gráfico 3: Contagem de Churn (Clientes que cancelaram vs. não cancelaram)
plt.figure(figsize=(8, 4))
sns.countplot(x='Churn', data=df)
plt.title("Contagem de Churn")
plt.xlabel("Churn")
plt.ylabel("Número de Clientes")
plt.show()

# Gráfico 4: Violin Plot de Total Pago por Churn
plt.figure(figsize=(8, 4))
sns.violinplot(x='Churn', y='Total_Pago', data=df)
plt.title("Distribuição de Total_Pago por Churn")
plt.xlabel("Churn")
plt.ylabel("Total Pago")
plt.show()

# Gráfico 5: Contagem de Idosos por Churn
plt.figure(figsize=(8, 4))
sns.countplot(x='Idoso', hue='Churn', data=df)
plt.title("Distribuição de Idosos por Churn")
plt.xlabel("Idoso (0 = Não, 1 = Sim)")
plt.ylabel("Número de Clientes")
plt.legend(title="Churn")
plt.show()

# Gráfico 6: Taxa média de Churn entre Idosos e Não Idosos
plt.figure(figsize=(8, 4))
sns.barplot(x="Idoso", y="Churn", data=df, ci=None)
plt.title("Taxa Média de Churn entre Idosos e Não Idosos")
plt.xlabel("Idoso (0 = Não, 1 = Sim)")
plt.ylabel("Média de Churn")
plt.show()

# 2D) Verificando balanceamento das variáveis booleanas
print("\nVerificando variáveis booleanas...")
bool_cols = [col for col in df.columns if df[col].dtype == 'bool' or set(df[col].unique()).issubset({0, 1})]
for col in bool_cols:
    print(f"\nDistribuição da variável '{col}':")
    print(df[col].value_counts())

# 3) Identificação e Tratamento de Outliers
print("\nTratando outliers usando o método IQR...")
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    num_outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col].count()
    print(f"Coluna: {col} - Número de outliers: {num_outliers}")

    # Removendo os outliers
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# 4A) Análise Bivariada

# Relação entre Tempo_de_Cliente e Churn
plt.figure(figsize=(8, 4))
sns.boxplot(x='Churn', y='Tempo_de_Cliente', data=df)
plt.title("Tempo_de_Cliente por Churn")
plt.xlabel("Churn")
plt.ylabel("Tempo de Cliente (meses)")
plt.show()

# Relação entre Pagamento Mensal e Churn
plt.figure(figsize=(8, 4))
sns.boxplot(x='Churn', y='Pagamento_Mensal', data=df)
plt.title("Pagamento Mensal por Churn")
plt.xlabel("Churn")
plt.ylabel("Pagamento Mensal")
plt.show()

# Relação entre Total_Pago e Churn (Violin Plot)
plt.figure(figsize=(8, 4))
sns.violinplot(x='Churn', y='Total_Pago', data=df)
plt.title("Distribuição de Total_Pago por Churn")
plt.xlabel("Churn")
plt.ylabel("Total Pago")
plt.show()

# Relação entre Tempo_de_Cliente e Total_Pago, separado por Churn
plt.figure(figsize=(8, 4))
sns.scatterplot(x='Tempo_de_Cliente', y='Total_Pago', hue='Churn', data=df)
plt.title("Relação entre Tempo_de_Cliente e Total_Pago")
plt.xlabel("Tempo de Cliente (meses)")
plt.ylabel("Total Pago")
plt.show()

# Relação entre Tipo de Contrato e Churn (Se a coluna existir)
if 'Tipo_Contrato' in df.columns:
    plt.figure(figsize=(8, 4))
    sns.countplot(x='Tipo_Contrato', hue='Churn', data=df)
    plt.title("Churn por Tipo de Contrato")
    plt.xlabel("Tipo de Contrato")
    plt.ylabel("Número de Clientes")
    plt.legend(title='Churn')
    plt.show()
else:
    print("\nA coluna 'Tipo_Contrato' não foi encontrada na base de dados.")

# 4B) Variáveis Mais Importantes para Previsão de Churn
print("\nVariáveis mais importantes para prever o Churn:")
print("- Tempo_de_Cliente: Clientes com menor tempo de relacionamento tendem a cancelar mais.")
print("- Pagamento_Mensal: Diferenças no valor pago mensalmente podem influenciar o cancelamento.")
print("- Total_Pago: O total pago pode indicar o nível de engajamento do cliente.")
print("- Idoso: A idade pode ser um fator relevante, dependendo da taxa de churn observada.")
print("- Tipo_Contrato: O tipo de contrato pode influenciar o churn, já que contratos mais longos podem reduzir a taxa de cancelamento.")

print("\nAnálise concluída!")
