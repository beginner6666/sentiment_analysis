# -*- coding: utf-8 -*-
import os
import pandas as pd
#path = "outbase/test_results.tsv"
data_path1 = 'data_dir/precredit0.tsv'
guids = []
#labels = [] 
#positive_score=[]
#neutral_score=[]
#negative_score=[]   
   
with open(data_path1,encoding='utf-8') as f1:
    for row in f1.readlines():
        if row[0].isalnum()==True:
            row = row.split('\t')
            guids.append(row[0])
           # guids.append('\n')
            #guids[row]=f1(row[0])
#with open(data_path1,encoding='utf-8') as f1:
    #for row in f1.readlines():
        #if row[0].isalnum()==True:
            #row = row.split('\t')
            #labels.append(row[1])
            
#with open ('submit.tsv','w',encoding='utf-8') as file:
    
    #file.write('id,title,label\n')
   # for guids in zip guids:
   #file.write("{}\n".format(guids))

#path1 = "data_dir/"
#pd_allid = pd.read_csv(os.path.join(path1, "precredit0.tsv") ,sep='\t',header=None)
#data = pd.DataFrame(columns=['label'])
#print(pd_allid.shape)
#for index in pd_allid.index:
   # id1 = pd_allid.loc[index].values[0]
            


path = "roberta_l24_large_model_out/"
#pd_all = pd.read_csv(os.path.join(path, "t.tsv") ,sep='\t',header=None)
pd_all = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)
data = pd.DataFrame(columns=['label'])
print(pd_all.shape)
for index in pd_all.index:
    positive_score = pd_all.loc[index].values[0]
    neutral_score = pd_all.loc[index].values[1]
    negative_score = pd_all.loc[index].values[2]

    if max(neutral_score, positive_score, negative_score) == positive_score:
        #labels.append('0')
            # data.append(pd.DataFrame([index, "neutral"],columns=['id','polarity']),ignore_index=True)
        data.loc[index+1] = ["0"]
    elif max(neutral_score, positive_score, negative_score) == neutral_score:
        #labels.append('1')
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
        data.loc[index+1] = [ "1"]
    else:
        #labels.append('2')
            #data.append(pd.DataFrame([index, "negative"],columns=['id','polarity']),ignore_index=True)
        data.loc[index+1] = [ "2"]           
            
labels=data.loc[:,'label']       
with open ('submit_robert.csv','w',encoding='utf-8') as file:
    #file.write('id,title,label\n')
    for guids,labels in zip(guids,labels):
        file.write("{},{}\n".format(guids,labels))
        




   # data.to_csv(os.path.join(path, "pre_sample.tsv"),sep = '\t')
    #print(data)

