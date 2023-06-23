import streamlit as st
import pandas as pd

def calcular_cr(notas):
    creditos_totais = 0
    soma_produto = 0

    for nota, creditos in notas:
        creditos_totais += creditos
        soma_produto += nota * creditos

    if creditos_totais == 0:
        return 0

    cr = soma_produto / creditos_totais
    return cr

def main():
    st.title("Cálculo do Coeficiente de Rendimento (CR)")
    
    # Entrada das notas e créditos das disciplinas
    notas = []
    i = 1  # Variável para gerar chaves únicas
    while True:
        nota = st.number_input("Nota da disciplina (0-10)", min_value=0.0, max_value=10.0, step=0.1, key=f"nota{i}")
        creditos = st.number_input("Créditos da disciplina", min_value=0.0, step=1.0, key=f"creditos{i}")
        if nota is None or creditos is None:
            break
        notas.append((nota, creditos))
        i += 1
    
    # Exibição do CR calculado
    if notas:
        cr = calcular_cr(notas)
        st.markdown(f"O Coeficiente de Rendimento (CR) é: **{cr:.2f}**")
    else:
        st.warning("Insira pelo menos uma disciplina.")

if __name__ == "__main__":
    main()

