import pandas as pd
import streamlit as st

df = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='PL')
st.dataframe(df)
