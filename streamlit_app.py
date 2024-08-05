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

'''with st.expander('Data visualisation'):
  df.columns = df.columns.str.strip()
  if 'Rating' in df.columns and 'Reviews' in df.columns:
    st.scatter_chart(data=df, x='Rating', y='Reviews')'''
  
#Input Features in sidebar
with st.sidebar:
  st.header('Input Features')
  category = st.selectbox('Category', ('AUTO_AND_VEHICLES', 'ART_AND_DESIGN', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS',
       'COMICS','COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FOOD_AND_DRINK', 'FAMILY', 'FINANCE',
       'GAME', 'HOUSE_AND_HOME', 'HEALTH_AND_FITNESS', 'LIBRARIES_AND_DEMO','LIFESTYLE', 'MEDICAL','NEWS_AND_MAGAZINES',
       'TOOLS', 'PARENTING', 'VIDEO_PLAYERS', 'PERSONALIZATION','PHOTOGRAPHY', 'SOCIAL', 'SPORTS', 
       'PRODUCTIVITY',  'TRAVEL_AND_LOCAL', 'SHOPPING','WEATHER', 'MAPS_AND_NAVIGATION'))
  rating = st.slider('Rating', 0,1., 1.2, 1.9, 5. , 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4. ,
       3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3. , 2.9, 2.8, 2.7,
       2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2. , 1.8, 1.7, 1.6, 1.5, 1.4,)

  type = st.electbox('Type', ('free', 'paid'))

  data = {'category' : category,
          'rating' : rating,
          'type' : type}

  input_df = pd.DataFrame(data, index[0])
  
