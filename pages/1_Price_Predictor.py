import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Gurgaon Price Predictor")

with open('/Users/dhirajsarswa/Documents/Real-State-Web/df.pkl', 'rb') as file:
      df = pickle.load(file)

st.dataframe(df)