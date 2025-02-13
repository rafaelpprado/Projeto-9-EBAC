# 📊 Análise de Churn em Telecom  

## 🔎 Prevendo Cancelamento de Clientes (Churn)  

Este projeto realiza uma **análise exploratória de dados  para identificar padrões que influenciam o **cancelamento de clientes** (**Churn**) em uma empresa de telecomunicações.  

O código inclui:  
✔️ **Carregamento e visualização da base de dados**  
✔️ **Análise estatística descritiva**  
✔️ **Identificação e tratamento de outliers**  
✔️ **Visualização de dados com gráficos**  
✔️ **Análise do impacto de variáveis como "Idoso" e "Tipo_Contrato" no Churn**  
✔️ **Destaque das variáveis mais importantes para previsão**  

---

## 📂 **Estrutura do Projeto**


📁 Churn-Telecom-Analysis
│── 📄 README.md  
│── 📄 projeto9.py  # Código Python da análise  
│── 📄 projeto8.csv  # Base de dados utilizada  

## 🔍 **Análises Realizadas**
### 1️⃣ **Carregamento dos Dados**
- ✔️ **Carreguei a base de dados `projeto8.csv` e visualizei as primeiras linhas para garantir que os dados foram importados corretamente.**

### 2️⃣ **Estatísticas Descritivas**
- ✔️ **Utilizei `describe()` para calcular estatísticas como média, mínimo, máximo e dispersão das variáveis numéricas.**

### 3️⃣ **Identificação e Tratamento de Outliers**
- ✔️ **Criei gráficos `boxplot` para visualizar outliers e apliquei o método `IQR` para removê-los, garantindo que valores extremos não distorçam as análises.**

### 4️⃣ **Análise Gráfica**
- ✔️ **Utilizei `seaborn` e `matplotlib` para criar visualizações e entender melhor os padrões dos dados:**
  - 📊 **Histograma do Tempo de Cliente vs. Churn**
  - 📈 **Boxplot do Pagamento Mensal por Churn**
  - 📊 **Contagem de Clientes que Cancelaram (Churn)**
  - 🎻 **Violin Plot do Total Pago por Churn**
  - 👴 **Distribuição de Clientes Idosos por Churn**
  - 📜 **Impacto do Tipo de Contrato no Churn**

### 5️⃣ **Identificação das Variáveis Mais Importantes**
- ✔️ **Analisando os gráficos e estatísticas, identifiquei as variáveis mais relevantes para prever o cancelamento de clientes (Churn):**
  - ⏳ **Tempo_de_Cliente** (Clientes com menor tempo de relacionamento tendem a cancelar mais)  
  - 💳 **Pagamento_Mensal** (Valores mais altos podem estar associados a taxas maiores de churn)  
  - 💰 **Total_Pago** (Clientes que gastaram menos ao longo do tempo podem ser mais propensos a sair)  
  - 👴 **Idoso** (Pode influenciar a decisão do cliente dependendo dos serviços oferecidos)  
  - 📜 **Tipo_Contrato** (Contratos mais longos tendem a reduzir o churn)  

---

## 📊 **Exemplos de Gráficos Gerados**
- ✔️ **Distribuição de Tempo de Cliente por Churn**  
- ✔️ **Relação entre Pagamento Mensal e Churn**  
- ✔️ **Churn por Tipo de Contrato**  

---

## 🚀 **Tecnologias Utilizadas**
- ✔️ **Python** - Linguagem principal do projeto  
- ✔️ **Pandas** - Manipulação de dados  
- ✔️ **NumPy** - Operações numéricas  
- ✔️ **Matplotlib** - Gráficos e visualizações  
- ✔️ **Seaborn** - Gráficos avançados  

---

## 📌 **Autor**
- 👤 **Rafael Prado**  
- 📧 **Email:** [rer.eu@hotmail.com](mailto:rer.eu@hotmail.com)  
- 🔗 **GitHub:** [rafaelpprado](https://github.com/rafaelpprado)  

Se gostou do projeto, **dê um ⭐️ star no repositório!** 🚀😊  

