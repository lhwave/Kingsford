import pandas as pd
import streamlit as st
import plotly.express as px

df_Income = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='Income', usecols='A:F')
df_Expense = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='Expense', usecols='A:F')
df_Profit = pd.read_excel(io='https://raw.githubusercontent.com/lhwave/kingsford/main/Data.xlsx', sheet_name='Profit', usecols='A:F')

st.subheader ('Kingsford Profit & Loss')

Years = df_Profit['Month'].unique().tolist()
Months = df_Profit['Month'].unique().tolist()
Month_selection = st.slider('Month selection:', min_value=min(Months), max_value=max(Months), value=(min(Months),max(Months)))

st.subheader('Income')

col1, col2 = st.columns(2)

with col1:
  st.radio(,key="Year_selection",options=["2023","2024"],)

mask= (df_Income['Month'].between(*Month_selection)) & (df_Income['Year']==(Year_selection)
df_Income_gp= df_Income[mask].groupby(by=['Account Name']).sum()[['Amount']]
df_Income_gp= df_Income_gp.reset_index()
fig = px.pie(df_Income_gp, values='Amount', names = 'Account Name')

with col2:
  st.plotly_chart(fig)

Income = df_Income['Account Name'].unique().tolist()
Income_selection = st.multiselect('Income selection:', Income, default=Income)
mask = (df_Income['Month'].between(*Month_selection)) & (df_Income['Account Name'].isin(Income_selection))


df_Income_gp = df_Income[mask].groupby(by=['Month','Year']).sum()[['Amount']]
df_Income_gp = df_Income_gp.reset_index()

fig = px.histogram(df_Income_gp, x='Month', y='Amount',
             color='Year', barmode='group')
fig.update_xaxes(type='category')
st.plotly_chart(fig)

st.subheader('Expense')

Expense = df_Expense['Account Name'].unique().tolist()
Expense_selection = st.multiselect('Expense selection:', Expense, default=Expense)
mask = (df_Expense['Month'].between(*Month_selection)) & (df_Expense['Account Name'].isin(Expense_selection))

df_Expense_gp = df_Expense[mask].groupby(by=['Month','Year']).sum()[['Amount']]
df_Expense_gp = df_Expense_gp.reset_index()

fig = px.histogram(df_Expense_gp, x='Month', y='Amount',
             color='Year', barmode='group')
fig.update_xaxes(type='category')
st.plotly_chart(fig)

st.subheader('Profit')

Profit = df_Profit['Account Name'].unique().tolist()
Profit_selection = st.selectbox('Profit selection:', Profit)
mask = (df_Profit['Month'].between(*Month_selection)) & (df_Profit['Account Name']==(Profit_selection))

df_Profit_gp = df_Profit[mask].groupby(by=['Month','Year']).sum()[['Amount']]
df_Profit_gp = df_Profit_gp.reset_index()

fig = px.histogram(df_Profit_gp, x='Month', y='Amount',
             color='Year', barmode='group')
fig.update_xaxes(type='category')
st.plotly_chart(fig)
