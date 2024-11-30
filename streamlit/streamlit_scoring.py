import streamlit as st
import pandas as pd
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np

# Custom Transformer para remoção de outliers
class OutlierHandler(BaseEstimator, TransformerMixin):
    def __init__(self, method='iqr'):
        self.method = method
        self.limits = None

    def fit(self, X, y=None):
        if self.method == 'iqr':
            self.limits = []
            for i in range(X.shape[1]):
                Q1 = X[:, i].quantile(0.25)
                Q3 = X[:, i].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                self.limits.append((lower, upper))
        return self

    def transform(self, X):
        X = X.copy()
        for i in range(X.shape[1]):
            lower, upper = self.limits[i]
            X[:, i] = np.clip(X[:, i], lower, upper)
        return X

# Função para carregar e preparar os dados
def preprocess_data(data, preprocessor):
    """Pré-processa os dados utilizando o pipeline"""
    return preprocessor.transform(data)

# Função principal do Streamlit
def main():
    st.title("Escoragem de Base de Dados - Credit Scoring")
    
    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Faça upload de um arquivo CSV para escoragem", type="csv")
    
    if uploaded_file is not None:
        # Lendo o CSV
        data = pd.read_csv(uploaded_file)
        st.write("Dados carregados:")
        st.dataframe(data.head())
        
        # Verificando se o modelo já foi salvo
        try:
            # Carregando o modelo treinado
            modelo_caminho = "modelo_credit_scoring.pkl"
            pipeline_model = joblib.load(modelo_caminho)
            st.success("Modelo carregado com sucesso!")
        except FileNotFoundError:
            st.error("Modelo treinado não encontrado. Certifique-se de salvar o modelo como 'modelo_credit_scoring.pkl'.")
            return
        
        # Definindo variáveis para pré-processamento
        variaveis_categoricas = [
            'sexo', 'posse_de_veiculo', 'posse_de_imovel', 'tipo_renda',
            'educacao', 'estado_civil', 'tipo_residencia'
        ]
        variaveis_numericas = ['qtd_filhos', 'idade', 'tempo_emprego', 'qt_pessoas_residencia', 'renda']
        
        # Garantindo que as variáveis necessárias estão presentes
        colunas_necessarias = variaveis_categoricas + variaveis_numericas
        if not set(colunas_necessarias).issubset(data.columns):
            st.error("As colunas necessárias estão ausentes no arquivo carregado.")
            return
        
        # Realizando a escoragem
        X = data[colunas_necessarias]
        scores = pipeline_model.predict_proba(X)[:, 1]  # Obtendo as probabilidades de "mau"
        
        # Adicionando os scores ao DataFrame
        data['score_mau'] = scores
        st.write("Dados escorados com os scores:")
        st.dataframe(data[['score_mau']].head())
        
        # Baixar os dados escorados
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Baixar Dados Escorados",
            data=csv,
            file_name="dados_escorados.csv",
            mime="text/csv",
        )

# Executando o app Streamlit
if __name__ == "__main__":
    main()
