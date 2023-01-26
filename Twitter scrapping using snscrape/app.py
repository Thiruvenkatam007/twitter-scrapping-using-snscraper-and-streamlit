import streamlit as st
from functions import scraping_text, upload_to_mongodb
import time


st.balloons()
st.header('Tweets scraping made easy')
st.image('Twitter-Anaylyze-Data-01.png')
st.subheader("""
Let's scrape some Tweets... :
""")

search_term = st.text_input('Please enter the search term here?')
since, until = st.date_input('Please enter the start date to search: '), \
                               st.date_input('please enter the finish date  :')
number_tweets = st.slider('How many tweets do you want to get?', 0, 5000, step=10)


submit_button = st.button('Search')
df = scraping_text(search_term=search_term, since=since, until=until, number_of_tweets=number_tweets)
if submit_button:
    st.write('First ten tweet data is showed here')
    st.progress(100)
    with st.spinner('Please wait while we getting your data.....'):
        time.sleep(5)
    st.dataframe(df.iloc[0:10])
    st.success(f'{search_term} data is successfully scraped from Twitter')
    

upload_button = st.button('Upload to MongoDB')
if upload_button:
    upload_to_mongodb(search_term=search_term)
    st.success(f'{search_term} data is successfully uploaded to MongoDB')


download = st.radio('Want to save file as CSV/JSON?', ['Yes', 'No'])
file_name = st.text_input('Name the file:')

if download == "Yes":
    choice = st.radio('Select file format:', ['CSV', 'JSON'])
    if choice == 'CSV':
        st.download_button(
            label="Download CSV",
            file_name=f"{file_name}.csv",
            mime="text/csv",
            data=df.to_csv()
        )
        st.success('CSV file is downloading.......')
    else:
        
        st.download_button(
            label="Download JSON",
            file_name=f"{file_name}.json",
            mime="application/json",
            data=df.to_json()
        )
        st.success('JSON file is downloading.......')
else:
    st.subheader('Have a good day and Thanks for visiting')
        
