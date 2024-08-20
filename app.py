import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='PL', usecols='A:F')

Months = df['Month'].unique().tolist()
Month_selection = st.slider("Month selection:", min_value=min(Months), max_value=max(Months), value=(min(Months),max(Months)))

mask = (df['Month'].between(*Month_selection))

df_gp = df[mask].groupby(by=['Month','Year']).sum()[['Amount']]

fig = px.histogram(df_gp, x='Month', y='Amount',
             color='Year', barmode='group')

st.plotly_chart(fig)
