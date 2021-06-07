import pandas as pd

import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Embedding, Flatten, Conv1D, MaxPooling1D, LSTM
from keras import utils
from keras.callbacks import ReduceLROnPlateau, EarlyStopping

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# import gensim

import re
import numpy as np
import os
from collections import Counter
import logging
import time
import pickle
import itertools

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# nltk.download('stopwords')

# DATASET
DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
DATASET_ENCODING = "ISO-8859-1"
TRAIN_SIZE = 0.8

# TEXT CLENAING
TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

# WORD2VEC 
W2V_SIZE = 300
W2V_WINDOW = 7
W2V_EPOCH = 32
W2V_MIN_COUNT = 10

# KERAS
SEQUENCE_LENGTH = 300
EPOCHS = 8
BATCH_SIZE = 1024

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)

# EXPORT
KERAS_MODEL = "model.h5"
WORD2VEC_MODEL = "model.w2v"
TOKENIZER_MODEL = "tokenizer.pkl"
ENCODER_MODEL = "encoder.pkl"

df = pd.read_csv("./datasets/training.2000.processed.noemoticon.csv", encoding =DATASET_ENCODING , names=DATASET_COLUMNS)
# print(len(df))
# print(df.head())

decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}

def decode_sentiment(label):
    return decode_map[int(label)]

df_target = df.target.apply(lambda x: decode_sentiment(x))
target_cnt = Counter(df_target)

# plt.figure(figsize=(16,8))
# plt.bar(target_cnt.keys(), target_cnt.values())
# plt.title("Dataset labels distribuition")