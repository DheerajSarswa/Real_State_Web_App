import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Gurgaon Price Predictor")

with open('/Users/dhirajsarswa/Documents/Real-State-Web/df.pkl', 'rb') as file:
      df = pickle.load(file)

with open('/Users/dhirajsarswa/Documents/Real-State-Web/pipeline.pkl', 'rb') as file:
      pipeline = pickle.load(file)


st.header('Enter your inputs')

# property type
property_type = st.selectbox('Property type', ['flat','house'])

# sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# bedroom
bedroom = float(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathroom = float(st.selectbox('Number of Bathroom', sorted(df['bathroom'].unique().tolist())))

# balcony
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

# age possession
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

# built up area
built_up_area = float(st.number_input("Built Up Area"))

# servant room
servant_room = 1.0 if (st.selectbox('Servant room', ['Yes','No']))=='Yes' else 0.0

# store room
store_room = 1.0 if (st.selectbox('Store room', ['Yes','No']))=='Yes' else 0.0

# furnishing type
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

# luxury category
luxury_category = st.selectbox('Luxury Type', sorted(df['luxury_category'].unique().tolist()))

# floor category
floor_category = st.selectbox('Floor Type', sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):

      # form a dataframe
      data = [[property_type, sector, bedroom, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
      columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'agePossession', 
                 'built_up_area', 'servant room', 'store room','furnishing_type',
                 'luxury_category', 'floor_category']
      one_df = pd.DataFrame(data=data, columns=columns)
      # predict
      base_price = (np.expm1(pipeline.predict(one_df)))[0]
      low = base_price - .2
      high = base_price + .2

      # display prediction
      st.text("The price of the flat is between {} Cr to {} Cr.".format(round(low,2),round(high,2)))