import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='PL')
df_gp = df[mask].groupby(by=['Acount Type']).sum()[['Amount']]
st.dataframe(df_gp)
