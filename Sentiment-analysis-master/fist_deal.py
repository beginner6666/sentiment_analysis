# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:57:02 2019

@author: User
"""

data_path1 = 'Train_DataSet.csv'
data_path2 = 'Train_DataSet_Label.csv'
guids1 = []
guids2 = []
text_as = []
text_asc = []
labels = []
with open(data_path2,encoding='utf-8') as f2:
    for row in f2.readlines():
        row = row.split(',')
        guids2.append(row[0])
        labels.append(int(row[1]))
       
        
with open(data_path1,encoding='utf-8') as f1:
    for row in f1.readlines():
        if row[0].isalnum()==True:
            row = row.split(',')
            guids1.append(row[0])
            text_as.append(row[1])
            text_asc.append(row[2])
            
        
with open ('credit.tsv','w',encoding='utf-8') as file:
    #file.write('id,title,label\n')
    for guids1,text_as,labels,text_asc in zip(guids1,text_as,labels,text_asc):
        file.write("{}\t{}\t{}\t{}".format(guids1,text_as,labels,text_asc))