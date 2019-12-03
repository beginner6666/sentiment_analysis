# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:40:48 2019

@author: User
"""
import pandas as pd
import re
import jieba
import string
train_data = pd.read_csv('Train_DataSet.csv')
train_label = pd.read_csv('Train_DataSet_Label.csv')
train = pd.merge(train_data, train_label, how='left', on='id')
train = train[(train.label.notnull()) & (train.content.notnull())]
test = pd.read_csv('Test_DataSet.csv')

train['title'] = train['title'].fillna('')
train['content'] = train['content'].fillna('')
test['title'] = test['title'].fillna('')
test['content'] = test['content'].fillna('')


def filter(text):
    text = re.sub("[A-Za-z0-9\!\=\？\%\[\]\,\（\）\>\<:&lt;\/#\. -----\_]", "", text)
    text = text.replace('图片', '')
    text = text.replace('\xa0', '') # 删除nbsp
    # new去除html标签
    r1 =  "\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\，。=？、：“”‘’￥……（）《》【】]"
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, ' ', text)        #去除html标签
    
    text = re.sub(r1,'',text)
    text = text.strip()
    return text

def clean_text(data):
    data['title'] = data['title'].apply(lambda x: filter(x))
    data['content'] = data['content'].apply(lambda x: filter(x))
    return data
train = clean_text(train)
test = clean_text(test)

stop_words = pd.read_table('stop.txt', header=None)[0].tolist()


table = str.maketrans("","",string.punctuation)
def cut_text(sentence):
    tokens = list(jieba.cut(sentence))
    # 去除停用词
    tokens = [token for token in tokens if token not in stop_words]
#   # 去除英文标点
#    
    return tokens
train_title = [cut_text(sent) for sent in train.title.values]
train_content = [cut_text(sent) for sent in train.content.values]
test_title = [cut_text(sent) for sent in test.title.values]
test_content = [cut_text(sent) for sent in test.content.values]
all_doc = train_title + train_content + test_title + test_content