import streamlit as st
import pandas as pd
st.write("Hello, *World!* :sunglasses:")

df = pd.read_csv('cars24-car-price.csv')
st.dataframe(df)
st.bar_chart(df, x="year", y="selling_price", stack=False)

st.scatter_chart(
    df,
    x="selling_price",
    y="km_driven"
)


title = st.selectbox(
    "Select your category to show",
    ("seller_type", "fuel_type", "transmission_type"),
)
st.write(title)
st.bar_chart(df, x="year", y="selling_price", stack=False)


