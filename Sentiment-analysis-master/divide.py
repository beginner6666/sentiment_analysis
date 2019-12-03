# -*- coding: utf-8 -*-
import random

def train_test_val_split(infile,val_rate=0.2,test_rate=0.1):
    with open('traina.tsv', 'w',encoding='utf-8') as f_train:
        with open('testa.tsv', 'w',encoding='utf-8') as f_test: 
            with open ('vala.tsv','w',encoding = 'utf-8') as f_val:
                
                for line in open(infile,encoding='utf-8'):
                    if random.random() > test_rate+val_rate:
                        f_train.write(line)
                    elif random.random() > test_rate:
                        f_val.write(line)
                    else:
                        f_test.write(line)


if __name__ == '__main__':
    train_test_val_split('c.tsv')
