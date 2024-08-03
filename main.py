#importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yt

#criar as funções de carregamento de dados
@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yt.Tickers(empresas)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

# prepara as visualizações
acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA","VALE3.SA", "ABEV3.SA", "GGBR4.SA" ]
dados  = carregar_dados(acoes)

# criar a interface do streamlit
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.      
""")
# prepaara as visualizações = filtros
lista_acoes = st.multiselect("Escolha as ações para visualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

# criar o grafico
st.line_chart(dados)