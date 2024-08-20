import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='PL', usecols='A:F')
df_gp = df.groupby(by=['Month','Year']).sum()[['Amount']]

fig = px.bar(df_gp, x='Month', y='Amount',
             color='Year')

st.plotly_chart(fig)
