import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Cargar modelo entrenado
modelo = joblib.load("modelo_gasolina.pkl")

# Cargar dataset para obtener lista de estados
# Use the df_melted DataFrame instead of loading from a file
estados = sorted(df_melted["Estado"].unique())

# Interfaz
st.title("📊 Estimador del precio de gasolina")

estado = st.selectbox("Selecciona un estado:", estados)
mes = st.slider("Selecciona un mes:", 1, 12, 6)
año = st.slider("Selecciona un año:", int(df_melted["Año"].min()), int(df_melted["Año"].max()), 2023)

# Convertir estado a código
estado_cod = df_melted[df_melted["Estado"] == estado]['Estado_Encoded'].iloc[0]

# Predicción
if st.button("Predecir precio"):
    # Reshape the input data to be a 2D array
    input_data = np.array([[estado_cod, mes, año]])
    prediccion = modelo.predict(input_data)
    st.metric("Precio estimado de gasolina", f"${prediccion[0]:.2f}")
