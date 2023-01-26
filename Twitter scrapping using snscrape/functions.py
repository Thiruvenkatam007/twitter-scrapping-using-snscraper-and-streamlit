import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools
from pymongo import MongoClient
import datetime

timestamp = datetime.datetime.now()



def scraping_text(search_term, since, until, number_of_tweets):
    
    scraped_tweets = sntwitter.TwitterSearchScraper(f'{search_term} since:{since} until:{until}').get_items()
    sliced_scraped_tweets = itertools.islice(scraped_tweets, number_of_tweets)
    global df
    df = pd.DataFrame(sliced_scraped_tweets)
    return df


def upload_to_mongodb(search_term):
    
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Twitter_scraping"]
    data = db["data"]

    data_dict = df.to_dict("records")
    data.insert_one({"index": f"{search_term} {timestamp}", "data": data_dict})
