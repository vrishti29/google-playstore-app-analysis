import streamlit as st
import pandas as pd
import numpy as np
#from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title = 'Interactive Data analysis')
st.title('Interactive EDA of Apps on Google Play Store')

with st.expander('About the app'):
  st.markdown("**What can this app do?**")
  st.info("")
  st.markdown('**How can you use the app?**')
  st.warning('To find the best suited app according to the input features.')

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
  #size
  installs = st.slider('Installs', min_value=-1, max_value=10000000000, value=(-1, 10000000000), step = 1000)
  type = st.selectbox('Type', ('Free', 'Paid'))
  content_rating = st.selectbox('Content Rating', ('Everyone', 'Everyone 10+', 'Teen', 'Mature 17+', 'Unrated', 'Adults only 18+'))
  #genres
  data = {'category' : category,
          'rating' : rating,
          'installs' : installs,
          'type' : type,
          'content rating' : content_rating
         }

  input_df = pd.DataFrame(data, index[0])
  input_features = pd.concat([input_df, X_raw], axis=0)
  
with st.expander('Input features'):
  st.write('**Input data**')
  input_df
  st.write('**Combined App data**')
  input_features

