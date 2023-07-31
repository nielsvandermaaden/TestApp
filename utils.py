import streamlit as st

from pydantic import BaseModel


# First test to get app online

st.header('App is online!!')

class DuikerTool(BaseModel):

  nr_1: float = 0

  nr_2: float = 0



  # First test function

  def add_numbers(self):

    nr_1 = self.nr_1

    nr_2 = self.nr_2

    

    new_nr = nr_1 + nr_2

    return new_nr



nr_1 = st.number_input('select nr 1')

nr_2 = st.number_input('select nr 2')



duiker = DuikerTool(nr_1=nr_1, nr_2=nr_2)



new_nr = duiker.add_numbers()

st.header(f"New nr = {new_nr}")

