import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Título e Introdução
st.title("Bem-vindo ao Meu Site com Streamlit! 🌟")
st.subheader("Este é um modelo interativo mostrando as funcionalidades do Streamlit.")

# Seção de Imagem
st.image(
    "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
    caption="Streamlit é incrível para criar interfaces de dados!",
    use_column_width=True,
)

# Upload de Arquivos
st.header("📤 Faça o Upload de um Arquivo")
uploaded_file = st.file_uploader("Envie um arquivo CSV", type=["csv"])
if uploaded_file:
    # Exibir os dados enviados
    df = pd.read_csv(uploaded_file)
    st.write("Aqui estão os dados do arquivo enviado:")
    st.dataframe(df)

# Gráficos Interativos
st.header("📊 Gráficos Interativos")
st.write("Vamos gerar alguns gráficos com dados fictícios:")

# Dados fictícios
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["A", "B", "C"]
)

# Seletor de Gráficos
chart_type = st.radio("Escolha o tipo de gráfico:", ("Linha", "Barra", "Histograma"))
if chart_type == "Linha":
    st.line_chart(data)
elif chart_type == "Barra":
    st.bar_chart(data)
else:
    fig, ax = plt.subplots()
    ax.hist(data["A"], bins=20, color="blue", alpha=0.7)
    st.pyplot(fig)

# Slider
st.header("🎚️ Ajuste Valores com Slider")
slider_val = st.slider("Escolha um número entre 1 e 100:", 1, 100, 50)
st.write(f"Você escolheu: {slider_val}")

# Simulação com Spinner
st.header("⏳ Simulação com Tempo de Espera")
if st.button("Clique para começar a simulação"):
    with st.spinner("Simulando..."):
        time.sleep(3)
    st.success("Simulação concluída!")

# Formulários e Input do Usuário
st.header("📝 Formulário")
with st.form("formulario"):
    nome = st.text_input("Seu Nome")
    email = st.text_input("Seu E-mail")
    opcao = st.selectbox("Qual é seu nível de experiência com Python?", ["Iniciante", "Intermediário", "Avançado"])
    enviado = st.form_submit_button("Enviar")
    if enviado:
        st.write(f"Olá, {nome}! Obrigado por preencher o formulário. Você é um usuário **{opcao}**.")

# Conclusão
st.header("🎉 Obrigado por visitar!")
st.write("Espero que você tenha gostado do modelo! Streamlit é uma ferramenta poderosa e fácil de usar para criar aplicativos de dados. 🚀")
