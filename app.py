import streamlit as st
import pandas as pd
import random

st.header('Turismo ETV1: Concón')
tipos = ['restaurant','hotel','museo']

tipo = random.choice(tipos)
st.write(tipo)

df = pd.read_html(f'http://quant.cl/places/Concón_{tipo}')[0]
st.dataframe(df)
