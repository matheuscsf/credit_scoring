# 📁 Diretório de Dados

Este diretório contém os dados utilizados no projeto **Credit Scoring**. Aqui está o conjunto de dados base para a análise, pré-processamento e treinamento do modelo.

---

## 📄 Arquivos Disponíveis

### 1️⃣ `credit_scoring.csv`

- **Descrição**: Este arquivo contém os dados utilizados para construir e validar o modelo de Credit Scoring.
- **Formato**: CSV (Comma-Separated Values).
- **Colunas Principais**:
  - `id_cliente` - Identificador único do cliente.
  - `sexo` - Sexo do cliente (`Masculino`, `Feminino`).
  - `posse_de_veiculo` - Possui veículo (`Sim`, `Não`).
  - `posse_de_imovel` - Possui imóvel próprio (`Sim`, `Não`).
  - `qtd_filhos` - Quantidade de filhos.
  - `renda` - Renda mensal declarada (em moeda local).
  - `educacao` - Nível de escolaridade do cliente.
  - `estado_civil` - Estado civil do cliente.
  - `tipo_renda` - Origem da renda (`Assalariado`, `Autônomo`, etc.).
  - `idade` - Idade do cliente.
  - `tempo_emprego` - Tempo de emprego atual (em anos).
  - `qt_pessoas_residencia` - Quantidade de pessoas na residência.
  - `mau` - Indicador de inadimplência (`Sim`, `Não`).

---

## 🧾 Informações Adicionais

- **Origem dos Dados**: Este conjunto de dados foi gerado para fins de estudo e validação do modelo de Credit Scoring.
- **Uso no Projeto**:
  - Os dados passam por etapas de pré-processamento, como tratamento de valores ausentes, remoção de outliers e codificação.
  - O modelo utiliza as colunas numéricas e categóricas para treinar e prever a probabilidade de inadimplência.
- **Privacidade**: Nenhum dado real de clientes foi utilizado. O dataset é fictício e segue boas práticas de anonimização.

---

## 🛠️ Como Utilizar os Dados

1. Coloque o arquivo `credit_scoring.csv` neste diretório (`data/`).
2. Garanta que o caminho para o arquivo esteja configurado corretamente nos notebooks ou scripts.
3. Utilize o arquivo como input no pipeline de pré-processamento e modelagem.

