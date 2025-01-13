import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título do site
st.title("Simulação de Lançamento de Projéteis 🚀")
st.write("""
Este aplicativo mostra como visualizar o lançamento de projéteis com anotações de pontos principais, vetores de velocidade e trajetórias, 
usando **matplotlib** integrado ao Streamlit.
""")

# Parâmetros do projétil
st.sidebar.header("Ajuste os Parâmetros do Projétil:")
velocidade_inicial = st.sidebar.slider("Velocidade Inicial (m/s):", 10, 100, 50)
angulo = st.sidebar.slider("Ângulo de Lançamento (°):", 10, 80, 45)
gravidade = st.sidebar.slider("Gravidade (m/s²):", 1.0, 20.0, 9.8)

# Cálculos básicos
angulo_rad = np.radians(angulo)
t_total = 2 * velocidade_inicial * np.sin(angulo_rad) / gravidade
t = np.linspace(0, t_total, num=100)
x_values = velocidade_inicial * np.cos(angulo_rad) * t
y_values = velocidade_inicial * np.sin(angulo_rad) * t - 0.5 * gravidade * t**2

# Ponto máximo
h_maxima = (velocidade_inicial**2) * (np.sin(angulo_rad)**2) / (2 * gravidade)
d_maxima = (velocidade_inicial**2) * np.sin(2 * angulo_rad) / gravidade

# Pontos de tempo e vetores
pontos_tempo = np.linspace(0, t_total, 5)
pontos_x = velocidade_inicial * np.cos(angulo_rad) * pontos_tempo
pontos_y = velocidade_inicial * np.sin(angulo_rad) * pontos_tempo - 0.5 * gravidade * pontos_tempo**2
velocidades_vx = [velocidade_inicial * np.cos(angulo_rad)] * len(pontos_tempo)
velocidades_vy = velocidade_inicial * np.sin(angulo_rad) - gravidade * pontos_tempo

# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, y_values, label="Trajetória de um Projétil", color="green")

# Marcações de H_max e d_max
ax.scatter([d_maxima / 2, d_maxima], [h_maxima, 0], color="blue", label="Pontos principais (H_max e d_max)")
ax.axhline(h_maxima, color="blue", linestyle="--", linewidth=0.7)
ax.axvline(d_maxima, color="blue", linestyle="--", linewidth=0.7)

# Vetores de Velocidade
for i in range(len(pontos_tempo)):
    label = "Velocidade (v)" if i == 0 else ""
    ax.quiver(
        pontos_x[i], pontos_y[i], velocidades_vx[i], velocidades_vy[i],
        angles="xy", scale_units="xy", scale=1, color="red", label=label
    )

# Pontos de tempo
for i, t in enumerate(pontos_tempo):
    ax.text(
        pontos_x[i],
        pontos_y[i] + 5,
        f"{t:.1f}s",
        fontsize=12,
        color="blue",
        ha="center"
    )

# Configurações finais do gráfico
ax.set_title("Lançamento de Projéteis")
ax.set_xlabel("Posição Horizontal (m)")
ax.set_ylabel("Posição Vertical (m)")
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.legend()
ax.grid()

# Mostrar gráfico no Streamlit
st.pyplot(fig)

# Explicação do gráfico
st.header("O que está acontecendo neste gráfico?")
st.write("""
1. **Trajetória de um Projétil**: A linha verde mostra a trajetória parabólica do projétil no espaço (posição horizontal vs. vertical).
2. **Pontos principais (H_max e d_max)**:
    - H_max: O ponto mais alto atingido pelo projétil.
    - d_max: A distância horizontal total do lançamento.
3. **Vetores de Velocidade**: As setas vermelhas indicam a velocidade do projétil em diferentes pontos da trajetória.
4. **Anotações de tempo**: Cada ponto azul é marcado com o tempo (em segundos) correspondente ao instante da trajetória.
""")

# Observações finais
st.success("Ajuste os parâmetros na barra lateral para explorar diferentes cenários!")
