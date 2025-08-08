import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="plotting Demo")
st. title('Analytics App')

st.header('Sector-Price per sqft GEO-MAP')

new_df = pd.read_csv('/Users/dhirajsarswa/Documents/Real-State-Web/Datasets/data_viz1.csv')
group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()


fig = px.scatter_mapbox(group_df, lat='latitude', lon='longitude', color='price_per_sqft', size='built_up_area', 
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10, 
                        mapbox_style='open-street-map', 
                        width=1200, height=700)
st.plotly_chart(fig, use_container_width=True) 


st.header('Features Wordcloud')
feature_text = pickle.load(open("/Users/dhirajsarswa/Documents/Real-State-Web/Datasets/feature_text.pkl",'rb'))
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='black',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot()

st.header('Area Vs Price')

property_type = st.selectbox('Select Property type',['flat','house'])

if property_type == 'house':
      fig1 = px.scatter(new_df[new_df['property_type']=='house'],
                        x='built_up_area', y='price', color='bedRoom', title='Area Vs Price')
else:
      fig1 = px.scatter(new_df[new_df['property_type']=='flat'],
                        x='built_up_area', y='price', color='bedRoom', title='Area Vs Price')

st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')

sector_options = sorted(new_df['sector'].unique().tolist())
sector_options.insert(0,'Overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector=='Overall':
      fig2 = px.pie(new_df, names='bedRoom')
else:
      fig2 = px.pie(new_df[new_df['sector']==selected_sector], names='bedRoom')

st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom']<=4], x='bedRoom', y='price', title="BHK Price Range")

st.plotly_chart(fig3, use_container_width=True)

st.header('Side by Side distribution plot for property type')

fig4 = plt.figure(figsize=(10,4))
sns.histplot(new_df[new_df['property_type']=='house']['price'], kde=True, bins=50, color='skyblue', label='House')
sns.histplot(new_df[new_df['property_type']=='flat']['price'], kde=True, bins=50, color='lightgreen', label='Flat')
plt.legend()
st.pyplot()