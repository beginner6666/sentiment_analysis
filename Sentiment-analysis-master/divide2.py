# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:30:52 2019

@author: User
"""

import random

def train_test_val_split(infile,val_rate=0.2):
    with open('train82.tsv', 'w',encoding='utf-8') as f_train:
        with open ('val82.tsv','w',encoding = 'utf-8') as f_val:
            for line in open(infile,encoding='utf-8'):
                if random.random() >= val_rate:
                        f_train.write(line)
                else:
                        f_val.write(line)



if __name__ == '__main__':
    train_test_val_split('credit.tsv')