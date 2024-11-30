# 🧠 Diretório de Modelos

Este diretório contém o modelo treinado utilizado para realizar a escoragem de dados no projeto **Credit Scoring**. O modelo é salvo no formato `.pkl` para ser carregado e utilizado na aplicação Streamlit.

---

## 📄 Arquivos Disponíveis

### 1️⃣ `modelo_credit_scoring.pkl`

- **Descrição**: Arquivo que contém o modelo de machine learning treinado e pronto para realizar previsões de inadimplência.
- **Formato**: Arquivo serializado no formato `pickle` (`.pkl`).

---

## 🚀 Como Gerar e Salvar o Modelo

1. **Treine o Modelo**  
   Use o notebook `notebooks/Mod38Projeto.ipynb` para realizar o treinamento. Certifique-se de que o pipeline está funcionando corretamente e que o modelo atinge métricas satisfatórias, como uma boa AUC-ROC.

2. **Salvar o Modelo**  
   Após o treinamento, utilize o código abaixo no notebook para salvar o modelo no diretório `models/`:
   ```python
   import joblib

   # Suponha que o pipeline treinado esteja na variável pipeline_model
   joblib.dump(pipeline_model, 'models/modelo_credit_scoring.pkl')
   print("Modelo salvo com sucesso!")

3. **Verifique o Arquivo**

Certifique-se de que o arquivo `modelo_credit_scoring.pkl` foi salvo corretamente no diretório `models/`.
