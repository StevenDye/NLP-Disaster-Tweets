"""This module is made for data cleaning and meta feature creataion"""
import pandas as pd

train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')


"""Creating meta features from the data"""

# Tweet length
train_df['length'] = train_df.text.apply(lambda x: len(str(x)))
test_df['length'] = test_df.text.apply(lambda x: len(str(x)))

# word count
train_df['word_count'] = train_df['text'].apply(lambda x: len(str(x).split()))
test_df['word_count'] = test_df['text'].apply(lambda x: len(str(x).split()))