import streamlit as st

st.title("IMC")
st.write("coloca ae")
altura = st.slider("Altura", 0.00, 2.50, value = 1.70)
peso = st.slider("Peso", 0.00, 300.0, value = 90.0)
butao = st.button("Calcular")

if butao:
    IMC = peso/(altura**2)
    st.markdown(f"O IMC é: **{IMC}**")
