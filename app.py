import streamlit as st 
from utils import DuikerTool

st.header('App runs from utils.py!!')

nr_1 = st.number_input('select nr 1')
nr_2 = st.number_input('select nr 2')

duiker = DuikerTool(nr_1=nr_1, nr_2=nr_2)
new_nr = duiker.add_numbers()

st.header(f"new nummero = {new_nr}")
