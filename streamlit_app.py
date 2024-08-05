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

with st.expander('Raw Data'):
  df

#Input Features in sidebar
with st.sidebar:
  st.header('Input Features')
  category = st.selectbox('Category', ('AUTO_AND_VEHICLES', 'ART_AND_DESIGN', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS',
       'COMICS','COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FOOD_AND_DRINK', 'FAMILY', 'FINANCE',
       'GAME', 'HOUSE_AND_HOME', 'HEALTH_AND_FITNESS', 'LIBRARIES_AND_DEMO','LIFESTYLE', 'MEDICAL','NEWS_AND_MAGAZINES',
       'TOOLS', 'PARENTING', 'VIDEO_PLAYERS', 'PERSONALIZATION','PHOTOGRAPHY', 'SOCIAL', 'SPORTS', 
       'PRODUCTIVITY',  'TRAVEL_AND_LOCAL', 'SHOPPING','WEATHER', 'MAPS_AND_NAVIGATION'))
  rating = st.slider('Rating', min_value=0.0, max_value=5.0, value=4.9, step=0.1)

  type = st.selectbox('Type', ('free', 'paid'))

  data = {'category' : category,
          'rating' : rating,
          'type' : type}

  input_df = pd.DataFrame(data, index[0])
  
