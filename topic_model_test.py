import re
import io
import gensim
import requests
import csv
import sqlite3

import Database_Helper

import Topic_Classifier_Utils as tcu
import tweepy

from CategoryIdentifier import Identifier
from Website import Website

consumer_key = "8v7yVO4eYM1FY7mlMPnEr2JjS"
consumer_secret = "VFxbvjsyRL29F2CmrymEDnfu9ZPmLCZcXDO5xDNy6mDnUWQFJZ"
access_token = "549478268-eD4N8lPJ6x9AgZAJkSdiqmQyHvsP8hw4tfjv24xi"
access_token_secret = "by3sNUoJ7Qd4Br83fOvbiIrpie6F6tSRm9nyZiSVpg3Si"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets_list = []
text_query = 'news'
count = 10000
csv_file_name = "meta-data/news_website_content.txt"

DATABASE_NAME = "meta-data/news_articles"

# Pulling individual tweets from query
db_helper = Database_Helper.Database_Helper()
db_helper.create_database(DATABASE_NAME, True)

iterator_key = 0
for tweet in api.search(q=text_query, count=count):
    tweet_text = tweet.text
    pattern = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"

    url = re.search(pattern,tweet_text)

    if url:
        my_website = Website(url.group(0))
        my_identifier = Identifier(my_website, "newsDetector.json")

        if my_identifier.is_match():
            print("{} is news.".format(my_website.website_url))

            body_text = ''
            for text in my_website.body_text:
                body_text = body_text + " " + text

            iterator_key = iterator_key + 1
            tuple_of_values = (iterator_key,my_website.website_url,tweet_text.encode("utf8"),body_text.encode("utf8"))
            db_helper.add_row(DATABASE_NAME,tuple_of_values)

db_helper.read_table(DATABASE_NAME, "NEWS")

'''
token_data = tcu.get_tokens_from_csv(csv_file_name, "meta-data/tokens", True)

dictionary = tcu.create_dictionary_from_tokens(token_data,'meta-data/dictionary', True)
corpus = tcu.create_a_corpus(dictionary, token_data,'meta-data/corpus', True)
lda_model = tcu.train_lda_model(corpus, 5, dictionary, 'meta-data/model5', True)

new_document = """Airlines have cancelled dozens of domestic and international flights as Storm Ciara approaches the UK.
Severe weather warnings have been issued for the weekend, with strong winds of up to 80mph and widespread heavy rain expected.
Several rail firms have urged passengers not to travel and say they will operate reduced timetables and speed restrictions on Sunday.
Ferry passengers also face disruption, as operators cancel some services.
Heathrow Airport announced it had taken the joint decision with its airline partners to "consolidate" Sunday's flight schedule in a bid to minimise the number of flights cancelled."""

new_document_topic = tcu.get_human_redable_topic_from_document(new_document, lda_model, dictionary)
print("The document: '{}' is type: '{}'".format(new_document,new_document_topic))
'''


