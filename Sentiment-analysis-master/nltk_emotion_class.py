# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:31:01 2019

@author: User
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
view = ["Great place to be when you are in Bangalore",
        "The place was being renovated when I visited so the seating was limited",
        "Loved the ambience, loved the food",
        "The place is not easy to locate"]
sid = SentimentIntensityAnalyzer()
for sen in view:
    print(sen)
    ss = sid.polarity_scores(sen)
    for k in ss:
        print('{0}:{1},'.format(k, ss[k]), end='')
    print()