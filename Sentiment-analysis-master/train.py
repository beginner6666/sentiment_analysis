# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from tqdm import tqdm
from keras.preprocessing.text import one_hot, Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasClassifier
from keras.layers import Dense, Flatten, Embedding, LSTM, SpatialDropout1D, Input, Bidirectional,Dropout, Activation, GRU
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical

train_data = pd.read_csv('Train_DataSet.csv',error_bad_lines=False)
train_label = pd.read_csv('Train_DataSet_Label.csv',error_bad_lines=False)
train = pd.merge(train_data, train_label, how='left', on='id')
train = train[(train.label.notnull()) & (train.content.notnull())]
test = pd.read_csv('Test_DataSet.csv',error_bad_lines=False)

train['title'] = train['title'].fillna('')
train['content'] = train['content'].fillna('')
test['title'] = test['title'].fillna('')
test['content'] = test['content'].fillna('')
