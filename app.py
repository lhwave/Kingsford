import pandas as pd
import streamlit as st

df = pd.read_excel(r'C:\Users\User\Documents\Excel_Webapp\Data.xlsx', sheet_name='PL')
st.dataframe(df)
