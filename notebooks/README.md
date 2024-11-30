# 📒 Diretório de Notebooks

Este diretório contém notebooks que documentam as etapas do projeto **Credit Scoring**. Os notebooks fornecem uma visão detalhada do pipeline de desenvolvimento, desde o carregamento dos dados até o treinamento e avaliação do modelo.

---

## 📄 Arquivos Disponíveis

### 1️⃣ `Mod38Projeto.ipynb`

- **Descrição**: Este notebook contém o fluxo completo do projeto, incluindo:
  - Carregamento e exploração inicial dos dados.
  - Pré-processamento: tratamento de valores ausentes, remoção de outliers, escalonamento e codificação.
  - Treinamento do modelo: utilização de algoritmos para prever a probabilidade de inadimplência.
  - Avaliação do modelo: análise de métricas como AUC-ROC, precisão e recall.
  - Salvamento do modelo treinado para deploy.

---

## 🛠️ Como Utilizar os Notebooks

1. **Configuração Inicial**:
   - Certifique-se de que os dados necessários estejam no diretório `data/` (ver [README de Dados](../data/README.md)).
   - Instale as dependências listadas em `requirements.txt`.

2. **Executando o Notebook**:
   - Abra o notebook no ambiente Jupyter, Google Colab ou outra ferramenta compatível.
   - Execute as células sequencialmente para reproduzir o pipeline completo.

3. **Modificações**:
   - O notebook é configurado para ser facilmente adaptável. Você pode ajustar o pipeline para incluir novos algoritmos ou etapas adicionais.

---

## 🔍 Objetivo do Notebook

O principal objetivo do notebook é servir como a documentação técnica e prática do projeto. Ele pode ser usado para entender a lógica do pipeline, ajustar parâmetros e reproduzir os resultados apresentados.
