import streamlit as st
import time

def main():
    st.title("Teste de Título")
    st.write("Texto...")

    st.header("Espaço de Texto:")
    input_text = st.text("Digite algo aqui:")

    if input_text:
        st.write("Você Digitou: ", input_text)


    # Testes de Seleção, box e slider:

    st.header("Seleção:")

    selection_box = st.selectbox("Selecione uma Opção:",
                                     ["Vermelho", "Azul", "Branco"])
    if selection_box:
        st.write("Você Selecionou:", selection_box)
    
    st.header("Seleção (Slider):")

    slider_box = st.slider(
        "Selecione um Valor:", 
            min_value = 0,
                max_value = 100,
                    value = 50
    )
    if slider_box:
        st.write(slider_box)
    
    st.header("Seleção (Slider de Valores Distintos):")


    # CheckBox:

    slider_d_box = st.select_slider("Selecione: ", 
                                    [10, 50, 100, 120])
    
    if slider_d_box:
        st.write(slider_d_box)

    st.header("CheckBox:")
    
    checkbox_state = st.checkbox("Aceito os Termos") 
    st.write("Estado da CheckBox:", checkbox_state)


    # Botões:

    st.header("Botões:")
    
    if st.button("Clique Aqui:", key = "button_1"):
        st.write("Botão Clicado!")
    

    # Loading:

    st.header("Loading:")

    with st.spinner("Wait"):
        time.sleep(3)
    st.success("Success!")

    if st.button("Clique Aqui:", key = "button_2"):
        with st.spinner("Wait"):
            time.sleep(3)
        st.success("Success!")


    # Upload de Arquivos:

    st.header("File Uploader:")
    uploaded_file = st.file_uploader("Choise a archive:", type = ["pdf", "jpeg"])

    if uploaded_file:
        st.write("The name of archive is: ", uploaded_file.name)


    # Gráficos:

    st.header("Gráficos:")
    data = {'x': [1, 2, 3, 4, 8], 'y': [10, 20, 80, 40, 50]}

    st.line_chart(data)
main()
