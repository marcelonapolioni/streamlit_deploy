import streamlit as st

st.title('Fazendo deploy')

slider = st.slider('Selecione um ano:', min_value=1995, max_value=2024 )
st.write(f'O ano selecionado foi: {slider}')

st.select_slider('selecione um ano: ', options=[1994, 1996, 2000, 2002, 2005, 2010])