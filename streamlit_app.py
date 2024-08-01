import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title = 'Interactive Data analysis')
st.title('Interactive EDA of Apps on Google Play Store')

with st.expander('About the app'):
  st.markdown("**What can thsi app do?**")
  st.info("")
  st.markdown('**How can you use the app?**')
  st.warning('To engage with the app.')

#Question header
st.header('Which Genre apps are performing best on Google Play Store?')

#Load data
df = pd.read_csv('https://raw.githubusercontent.com/vrishti29/google-playstore-app-analysis/master/data/googleplaystore.csv')
