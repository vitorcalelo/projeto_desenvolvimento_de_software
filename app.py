import pandas as pd
import plotly.express as px
import streamlit as st

# Título e cabeçalho do app
st.header('Análise de Dados de Veículos US')

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Opção 1: Usando Caixas de Seleção (Checkbox)
st.write('Selecione os gráficos que deseja visualizar:')

# Caixa de seleção para o histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odômetro (odometer)...')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão (Preço vs Odômetro)...')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
