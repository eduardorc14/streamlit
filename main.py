#importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yt

#criar as funções de carregamento de dados
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yt.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao

# prepara as visualizações
dados  = carregar_dados("ITUB4.SA")
print(dados)
# criar a interface do streamlit
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos.      
""")

# criar o grafico
st.line_chart(dados)