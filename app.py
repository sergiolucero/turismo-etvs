import streamlit as st
import pandas as pd
import time

t0=time.time()
st.header('Turismo ETV1: Concón')

tipos = ['restaurant','hotel','museo'] #,'teatro','galeria']
if False:
    xdf = pd.DataFrame()
    for tipo in tipos:
      url = f'http://quant.cl/places/Concon_{tipo}'
      df = pd.read_html(url, encoding='utf-8')[0]
      df['tipo'] = tipo
      df = df.drop(columns=['opening_hours'])
      xdf = xdf.append(df)

    gdf = xdf.groupby('tipo').size()
else:
    xdf = pd.read_csv('xdf3t.csv')
    gdf = pd.read_pickle('gdf3t.pk')
    
st.write('DT:', round(time.time()-t0,2))
st.dataframe(xdf)   
st.dataframe(gdf)
# either map or grab map from url above!
