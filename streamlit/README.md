# 🎛️ Diretório Streamlit

Este diretório contém o código da aplicação Streamlit desenvolvida para realizar a escoragem de dados no projeto **Credit Scoring**. A aplicação permite que os usuários façam upload de um arquivo CSV e obtenham os scores de inadimplência.

---

## 📄 Arquivos Disponíveis

### 1️⃣ `streamlit_scoring.py`

- **Descrição**: Código principal da aplicação Streamlit.
  - Carrega o modelo treinado (`modelo_credit_scoring.pkl`).
  - Permite o upload de um arquivo CSV.
  - Realiza a escoragem dos dados.
  - Gera um arquivo CSV com os scores adicionados.

---

# 🚀 Como Rodar a Aplicação

1. Navegue até o diretório raiz do projeto:

- `cd credit-scoring-project`

2. Execute o Streamlit:

- `streamlit run streamlit/streamlit_scoring.py`

3. Acesse o aplicativo no navegador, geralmente disponível em:

- `http://localhost:8501`

---

# 🎯 Funcionalidades da Aplicação

- Upload de Arquivo: Faça upload de um arquivo CSV com os dados que deseja escorar.

- Visualização de Dados: Visualize os primeiros registros do arquivo carregado.

- Geração de Scores: O modelo calcula a probabilidade de "mau" para cada cliente.

- Download de Resultados: Baixe um novo arquivo CSV com a coluna `score_mau` adicionada.
