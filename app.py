import streamlit as st
import pandas as pd
import random

st.header('Turismo ETV1: Concón')
tipos = ['restaurant','hotel','museo']

tipo = random.choice(tipos)
st.write(tipo)

url = f'http://quant.cl/places/Concon_{tipo}'
df = pd.read_html(url, encoding='utf-8')[0]
st.dataframe(df)   

# either map or grab map from url above!
