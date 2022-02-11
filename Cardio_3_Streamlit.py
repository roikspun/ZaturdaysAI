import pandas as pd
import numpy as np
# import seaborn as sns
import streamlit as st
# import matplotlib as plt

cardio = pd.read_csv('cardio_train.csv', sep=';')
cardio.shape 

st.write("My first Streamlit App")
st.dataframe(cardio)

