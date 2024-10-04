
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title for the Streamlit App
st.title('Bike Sharing Rental Analysis')

# Load the dataset
data_hour = pd.read_csv('E:\Project 1 Bangkit\hour.csv')
data_day = pd.read_csv('E:\Project 1 Bangkit\day.csv')
# Title for the Streamlit App
st.title('Bike Sharing Rental Analysis')

option = st.sidebar.selectbox('choose dataset', ('Hour', 'Day'))
if option == 'Hour':
    st.write('Selected hourly dataset')
    data = data_hour
else:
    st.write('Selected daily dataset')
    data = data_day


# Show raw data on user request
if st.checkbox('Show raw data'):
    st.write(data)

# Basic statistics about the data
st.subheader('Dataset Description')
st.write(data.describe())

# Visualization: User Count Distribution by Season
st.subheader('User Count Distribution by Season')
season_count = data.groupby('season')['cnt'].sum()
fig1, ax1 = plt.subplots()
ax1.bar(season_count.index, season_count.values, color='blue')
ax1.set_xlabel('Season')
ax1.set_ylabel('User Count')
ax1.set_title('Total User Count per Season')
st.pyplot(fig1)

# Visualization: User Count Distribution by Weather Condition
st.subheader('User Count Distribution by Weather Condition')
weather_count = data.groupby('weathersit')['cnt'].sum()
fig2, ax2 = plt.subplots()
ax2.bar(weather_count.index, weather_count.values, color='green')
ax2.set_xlabel('Weather Condition')
ax2.set_ylabel('User Count')
ax2.set_title('Total User Count by Weather Condition')
st.pyplot(fig2)

# Visualization: Monthly Trends
st.subheader('Monthly Trends in User Count')
month_count = data.groupby('mnth')['cnt'].sum()
fig3, ax3 = plt.subplots()
ax3.plot(month_count.index, month_count.values, marker='o', linestyle='-', color='purple')
ax3.set_xlabel('Month')
ax3.set_ylabel('User Count')
ax3.set_title('User Count per Month')
st.pyplot(fig3)

# Additional Insights
st.subheader('Additional Insights')
st.write('1. The highest number of bike rentals occur during season 3 (fall).')
st.write('2. The lowest number of bike rentals occur during season 4 (winter).')
st.write('3. Users prefer renting bikes during clear weather (weathersit 1).')
st.write('4. The best revenue is achieved with user counts in the higher range.')
st.write('5. There is a noticeable drop in users during the months of October, November, and December.')

# Note: Ensure that the dataset and column names match the ones in your notebook for accurate visualization.
