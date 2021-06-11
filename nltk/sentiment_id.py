from os import replace
from nltk.util import pr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

import twint
import nest_asyncio

import datetime as dt
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk
# nltk.download('punkt')

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# from wordcloud import WordCloud

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Embedding, Dense, Dropout, LSTM
from keras.optimizers import Adam, RMSprop, SGD
from keras.callbacks import EarlyStopping
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

seed = 0
np.random.seed(seed)

sns.set(style = 'whitegrid')

nest_asyncio.apply()

tweets_data = pd.read_csv('../datasets/tweet_covid.csv')
# print(tweets_data.head())

tweets = tweets_data[['conversation_id', 'date', 'time', 'user_id', 'username', 'tweet', 'mentions', 'replies_count', 'retweets_count', 'likes_count', 'hashtags', 'translated']]
# print(tweets)

def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # remove mentions
    text = re.sub(r'#[A-Za-z0-9]+', '', text) # remove hashtag
    text = re.sub(r'RT[\s]', '', text) # remove RT
    text = re.sub(r"http\S+", '', text) # remove link
    text = re.sub(r'[0-9]+', '', text) # remove numbers

    text = text.replace('\n', ' ') # replace new line into space
    text = text.translate(str.maketrans('', '', string.punctuation)) # remove all punctuations
    text = text.strip(' ') # remove characters space from both left and right text
    return text

def casefoldingText(text): # Converting all the characters in a text into lower case
    text = text.lower() 
    return text

def tokenizingText(text): # Tokenizing or splitting a string, text into a list of tokens
    text = word_tokenize(text) 
    return text

def filteringText(text): # Remove stopwors in a text
    listStopwords = set(stopwords.words('indonesian'))
    filtered = []
    for txt in text:
        if txt not in listStopwords:
            filtered.append(txt)
    text = filtered 
    return text

def stemmingText(text): # Reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = [stemmer.stem(word) for word in text]
    return text

def toSentence(list_words): # Convert list of words into sentence
    sentence = ' '.join(word for word in list_words)
    return sentence

# Preprocessing tweets data
tweets['text_clean'] = tweets['tweet'].apply(cleaningText)
tweets['text_clean'] = tweets['text_clean'].apply(casefoldingText)
tweets.drop(['tweet'], axis=1, inplace=True)

tweets['text_preprocessed'] = tweets['text_clean'].apply(tokenizingText)
tweets['text_preprocessed'] = tweets['text_preprocessed'].apply(filteringText)
tweets['text_preprocessed'] = tweets['text_preprocessed'].apply(stemmingText)

tweets.drop_duplicates(subset='text_clean', inplace=True)

tweets.to_csv(r'./datasets/tweets_data_clean.csv', index = False, header = True,index_label=None)

# tweets = pd.read_csv('tweets_data_clean.csv')

# for i, text in enumerate(tweets['text_preprocessed']):
#     tweets['text_preprocessed'][i] = tweets['text_preprocessed'][i].replace("'", "")\
#                                             .replace(',','').replace(']','').replace('[','')
#     list_words=[]
#     for word in tweets['text_preprocessed'][i].split():
#         list_words.append(word)
        
#     tweets['text_preprocessed'][i] = list_words
    
# lexicon_positive = dict()
# with open('../datasets/lexicon_positive.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         lexicon_positive[row[0]] = int(row[1])

# lexicon_negative = dict()
# with open('../datasets/lexicon_negative.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         lexicon_negative[row[0]] = int(row[1])

# def sentiment_analysis_lexicon_indonesia(text):
#     #for word in text:
#     score = 0
#     for word in text:
#         if (word in lexicon_positive):
#             score = score + lexicon_positive[word]
#     for word in text:
#         if (word in lexicon_negative):
#             score = score + lexicon_negative[word]
#     polarity=''
#     if (score > 0):
#         polarity = 'positive'
#     elif (score < 0):
#         polarity = 'negative'
#     else:
#         polarity = 'neutral'
#     return score, polarity

# results = tweets['text_preprocessed'].apply(sentiment_analysis_lexicon_indonesia)
# results = list(zip(*results))
# tweets['polarity_score'] = results[0]
# tweets['polarity'] = results[1]
# print(tweets)