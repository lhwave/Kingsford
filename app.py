import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='PL', usecols='A:F')
df_gp = df.groupby(by=['Month','Year']).sum()[['Amount']]

Month = df[‘Month’].unique().tolist()
Month_selection = st.slider(‘Month selection:’, min_value=min(month), max_value=max(month), value=(min(month),Max(month)))

fig = px.histogram(df, x='Month', y='Amount',
             color='Year', barmode='group')

st.plotly_chart(fig)
