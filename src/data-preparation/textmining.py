import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

data = pd.read_csv('../../gen/data-preparation/temp/KLM-direct_tweets.csv', sep = '\t')
data.head()

analyser = SentimentIntensityAnalyzer()
for i, j in data.iterrows():
    print(i)
    try:
        vs = analyser.polarity_scores(j['text'])
        data.loc[i, 'neg'] = vs['neg']
        data.loc[i, 'neu'] = vs['neu']
        data.loc[i, 'pos'] = vs['pos']
        data.loc[i, 'compound'] = vs['compound']
    except:
        data.loc[i, 'neg'] = ''
        data.loc[i, 'neu'] = ''
        data.loc[i, 'pos'] = ''
        data.loc[i, 'compound'] = ''

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset_direct_tweets.csv', index = False)

print('done analysis direct tweets')

data = pd.read_csv('../../gen/data-preparation/temp/KLM-re_tweets.csv', sep = '\t')
data.head()

analyser = SentimentIntensityAnalyzer()
for i, j in data.iterrows():
    print(i)
    vs = analyser.polarity_scores(j['text'])
    data.loc[i, 'neg'] = vs['neg']
    data.loc[i, 'neu'] = vs['neu']
    data.loc[i, 'pos'] = vs['pos']
    data.loc[i, 'compound'] = vs['compound']


data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset_re_tweets.csv', index = False)

print('done analysis retweets')
