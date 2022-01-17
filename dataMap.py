import numpy as np
import pandas as pd
import streamlit as st
import altair as alt


st.set_page_config(layout="wide")

dataFrame = pd.DataFrame(np.random.randn(2000, 2) / [10, 10] + [43.65, -79.34], columns=['lat', 'lon'])

if st.checkbox('Show dataframe'):
     st.map(dataFrame)
print(dataFrame)

st.map(dataFrame)
