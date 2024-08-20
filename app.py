import pandas as pd
import streamlit as st
import plotly.express as px

df_Income = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='Income', usecols='A:F')
df_Expense = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='Expense', usecols='A:F')
df_Profit = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='Profit', usecols='A:F')

st.subheader ('Kingsford's Profit & Loss')

Months = df['Month'].unique().tolist()
Month_selection = st.slider('Month selection:', min_value=min(Months), max_value=max(Months), value=(min(Months),max(Months)))

st.subheader('Income')

Income = df_Income['Account Name'].unique().tolist()
Income_selection = st.multiselect('Income selection:', Income, default=Income)
mask = (df_Income['Month'].between(*Month_selection)) & (df_Income['Account Name'].isin(Income_selection))

df_Income_gp = df[mask].groupby(by=['Month','Year']).sum()[['Amount']]
df_Income_gp = df_Income_gp.reset_index()

fig = px.histogram(df_gp, x='Month', y='Amount',
             color='Year', barmode='group')
fig.update_xaxes(type='category')
st.plotly_chart(fig)
