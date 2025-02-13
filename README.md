Análise de Churn em Telecom
📊 Prevendo Cancelamento de Clientes (Churn)
📖 Sobre o Projeto
Este projeto realiza uma análise exploratória de dados em uma base de Churn de Telecom. O objetivo é identificar padrões que influenciam o cancelamento de clientes (Churn) e destacar as variáveis mais importantes para prever esse comportamento.

O código inclui: 
✅ Carregamento e visualização da base de dados
✅ Análise estatística descritiva
✅ Identificação e tratamento de outliers
✅ Visualização de dados com gráficos
✅ Análise do impacto de variáveis como "Idoso" e "Tipo_Contrato" no Churn
✅ Destaque das variáveis mais importantes para previsão

📁 Churn-Telecom-Analysis
│── 📄 README.md  
│── 📄 projeto8.py  # Código Python da análise  
│── 📄 projeto8.csv  # Base de dados utilizada  
🔍 Análises Realizadas

1️⃣ Carregamento dos Dados
📌 Carreguei a base de dados projeto8.csv e visualizei as primeiras linhas.

2️⃣ Estatísticas Descritivas
📌 Usei describe() para analisar médias, mínimos, máximos e a distribuição das variáveis.

3️⃣ Identificação e Tratamento de Outliers
📌 Utilizei boxplots para identificar outliers e apliquei o método IQR para removê-los.

4️⃣ Análise Gráfica
📌 Utilizei seaborn e matplotlib para visualizar padrões nos dados, incluindo:

📊 Histograma do Tempo de Cliente vs. Churn
📈 Boxplot do Pagamento Mensal por Churn
📊 Contagem de Churn
📉 Violin plot do Total Pago por Churn
👴 Distribuição de Idosos por Churn
📜 Análise do impacto do Tipo de Contrato no Churn
5️⃣ Variáveis Mais Importantes
📌 Identifiquei as variáveis mais relevantes para prever o cancelamento de clientes:

⏳ Tempo_de_Cliente
💳 Pagamento_Mensal
💰 Total_Pago
👴 Idoso
📜 Tipo_Contrato
📊 Exemplos de Gráficos Gerados
📌 Churn por Tipo de Contrato

📌 Distribuição de Tempo de Cliente por Churn

📌 Relação entre Pagamento Mensal e Churn

🚀 Tecnologias Utilizadas
🔹 Python - Linguagem principal do projeto
🔹 Pandas - Manipulação de dados
🔹 NumPy - Operações numéricas
🔹 Matplotlib - Gráficos e visualizações
🔹 Seaborn - Gráficos avançados

👤 Rafael Prado
📧 Email: rer.eu@hotmail.com
🔗 GitHub: rafaelpprado
Se gostou do projeto, ⭐️ dê um star no repositório! 😊🚀
