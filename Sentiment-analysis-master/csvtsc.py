# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:10:13 2019

@author: User
"""

class IMDBProcessor(DataProcessor):
    """
    IMDB data processor
    """
    
    def __init__(self):
        self.labels = ["0","1","2"]
        
        
    def _read_csv(self, data_dir, file_name):
        with tf.gfile.Open(data_dir + file_name, "r") as f:
            reader = csv.reader(f, delimiter=",", quotechar=None)
            lines = []
            for line in reader:
                lines.append(line)

        return lines

    def get_train_examples(self, data_dir):
        lines = self._read_csv(data_dir, "train.csv")

        examples = []
        for line in enumerate(lines):
            
            
           # if i == 0:
               # continue
           # guid = "train-%d" % (i)
           text_a = tokenization.convert_to_unicode(line[0])
           text_a = tokenization.convert_to_unicode(line[1])
           label = tokenization.convert_to_unicode(line[2])
           examples.append(
                InputExample(guid=guid, text_a=text_a, label=label))
        return examples

    def get_dev_examples(self, data_dir):
        lines = self._read_csv(data_dir, "val.csv")

        examples = []
        for line in enumerate(lines):
            #if i == 0:
               # continue
            #guid = "dev-%d" % (i)
            guid = tokenization.convert_to_unicode(line[0])
            text_a = tokenization.convert_to_unicode(line[1])
            label = tokenization.convert_to_unicode(line[2])
            examples.append(
                InputExample(guid=guid, text_a=text_a, label=label))
        return examples

    def get_test_examples(self, data_dir):
        lines = self._read_csv(data_dir, "test.csv")

        examples = []
        for line in enumerate(lines):
           # if i == 0:
                #continue
            #guid = "test-%d" % (i)
            guid = tokenization.convert_to_unicode(line[0])
            text_a = tokenization.convert_to_unicode(line[1])
            label = tokenization.convert_to_unicode(line[2])
            examples.append(
                InputExample(guid=guid, text_a=text_a, label=label))
        return examples
    
    def get_labels(self):
        return self.labels