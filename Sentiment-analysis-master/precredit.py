# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:28:28 2019

@author: User
"""

data_path1 = 'Test_DataSet.csv'

guids = []

text_as = []
text_asc = []
labels = []        
with open(data_path1,encoding='utf-8') as f1:
    for row in f1.readlines():
        if row[0].isalnum()==True:
            row = row.split(',')
            guids.append(row[0])
            text_as.append(row[1])
            labels.append(0)
            text_asc.append(row[2])
            
        
with open ('precredit0.tsv','w',encoding='utf-8') as file:
    #file.write('id,title,label\n')
    for guids,text_as,labels,text_asc in zip(guids,text_as,labels,text_asc):
        file.write("{}\t{}\t{}\t{}".format(guids,text_as,labels,text_asc))
     #for guids,text_as in zip(guids,text_as):
        #file.write("{}\t{}\n".format(guids,text_as))