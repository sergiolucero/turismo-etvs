import streamlit as st
import pandas as pd

st.header('Turismo ETV1: Concón')
tipos = ['restaurant','hotel','museo'] #,'teatro','galeria']

xdf = pd.DataFrame()
for tipo in tipos:
  url = f'http://quant.cl/places/Concon_{tipo}'
  df = pd.read_html(url, encoding='utf-8')[0]
  df['tipo'] = tipo
  #df = df.drop(columns=['open'])
  xdf = xdf.append(df)
  
gdf = xdf.groupby('tipo').size()
st.dataframe(xdf)   
st.dataframe(gdf)
# either map or grab map from url above!
