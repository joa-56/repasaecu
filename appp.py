import streamlit as st
import random

# Función para generar ecuación
def generar_ecuacion():
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 10)

    c = a * x + b
    return a, b, c, x

# Mantener estado
if "ecuacion" not in st.session_state:
    st.session_state.ecuacion = generar_ecuacion()

a, b, c, respuesta_correcta = st.session_state.ecuacion

st.title("❄️ Practica ecuaciones de primer grado")

st.write(f"Resuelve:  {a}x + {b} = {c}")

respuesta = st.number_input("Tu respuesta (x):", step=1)

if st.button("Verificar"):
    if respuesta == respuesta_correcta:
        st.success("¡Correcto! 🎉")
        st.snow()  # NIEVE ❄️
        
        # Nueva ecuación
        st.session_state.ecuacion = generar_ecuacion()
    else:
        st.error("Incorrecto, intenta otra vez 😢")

if st.button("Nuevo ejercicio"):
    st.session_state.ecuacion = generar_ecuacion()
