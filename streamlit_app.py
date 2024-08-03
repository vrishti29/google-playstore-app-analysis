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

with st.expander('Data visualisation'):
  df.columns = df.columns.str.strip()
  if 'Rating' in df.columns and 'Reviews' in df.columns:
    st.scatter_chart(data=df, x='Rating', y='Reviews')
  
#Input Features in sidebar
with st.sidebar:
  st.header('Input Features')
  category = st.selectbox('Category', ('ART_AND_DESIGN', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS',
       'COMICS', 'DATING', 'EDUCATION', 'EVENTS', 'FOOD_AND_DRINK',
       'HOUSE_AND_HOME', 'LIBRARIES_AND_DEMO', 'FAMILY', 'MEDICAL',
       'TOOLS', 'PARENTING', 'VIDEO_PLAYERS', 'PERSONALIZATION', 'GAME',
       'PHOTOGRAPHY', 'SOCIAL', 'SPORTS', 'COMMUNICATION', 'PRODUCTIVITY',
       'AUTO_AND_VEHICLES', 'FINANCE', 'LIFESTYLE', 'TRAVEL_AND_LOCAL',
       'SHOPPING', 'HEALTH_AND_FITNESS', 'WEATHER', 'NEWS_AND_MAGAZINES',
       'MAPS_AND_NAVIGATION', 'ENTERTAINMENT'))
  with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
