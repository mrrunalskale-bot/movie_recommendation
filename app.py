import streamlit as st
import pandas as pd
import pickle as pkl
import math
pipe = pkl.load(open("cpp.pkl","rb+"))

st.title("Car Price Prediction Project")
df = pd.read_csv("clean_data.csv")
companies = sorted(df["company"].unique())
company = st.selectbox('Enter company ',companies)

names = sorted(df[df['company']==company]['name'].unique())
name = st.selectbox('Enter name ',names)

year = st.number_input('Enter year ',min_value=2005,max_value=2025)

kms_driven = st.number_input('enter kms_driven ',min_value=500)

fuel_types = sorted(df[df["name"]==name]["fuel_type"].unique())
fuel_type = st.selectbox('Enetr fuel type',fuel_types)

if st.button('Predict'):
    data = [[name,company,year,kms_driven,fuel_type]]
    columns = ['name','company','year','kms_driven','fuel_type']
    myinput = pd.DataFrame(data=data,columns=columns) 
    result = pipe.predict(myinput)
    result = result[0,0]
    value = math.ceil(result)
    st.text(f"₹{value:,}")