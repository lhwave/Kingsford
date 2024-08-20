import pandas as pd
import plotly_express as px
import streamlit as st

URL= r'C:\Users\User\Documents\Excel_Webapp\Data.xlsx'

df = pd.read_excel(r'C:\Users\User\Documents\Excel_Webapp\Data.xlsx', sheet_name='PL')

st.dataframe(df)