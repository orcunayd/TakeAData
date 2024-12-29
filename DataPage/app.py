import streamlit as st

symbol = st.sidebar.text_input('Hisse Senedi Sembolü', value = 'GOOGL')

st.title(symbol + ' Hisse Senedi Grafiği')
