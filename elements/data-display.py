import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)
st.table(data=df)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})