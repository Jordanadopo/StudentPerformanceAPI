import pandas as pd
import numpy as np
from sklearn import tree


class Performer:
    #according to investigations
    #by default we use portuguese course dataset
    #use 5 for binary tree best max_depth for portuguese course performance
    max_depth=5
    #use 500 for rows lines shuffled for training (60% of dataset) 
    max_train_line=500
    
    #load dataset of student portuguese scores
    d = pd.read_csv('dataset/student-por.csv', sep=';')


    def __init__(self, course='por'):
        if course=='mat':
            d = pd.read_csv('dataset/student-mat.csv', sep=';')
            #use 11 for binary tree best max_depth for math course performance
            max_depth=11
            #use 200 for rows lines shuffled for training (60% of dataset) 
            max_train_line=200

        #generate binary label (pass/fail) based on G1+G2+G3 (test grades, each 0-20 pts); threshold for passing is sum>=30
        d['pass'] = d.apply(lambda row: 1 if(row['G1'] + row['G2']+ row['G3']) >= 35 else 0, axis=1)

        #drop periods marks column
        d = d.drop(['G1', 'G2', 'G3'], axis=1)

        #one-hot encoding on categorical columns
        d = pd.get_dummies(d, columns=['sex', 'school', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
                                    'nursery', 'higher', 'internet', 'romantic'])

        #shuffle rows
        d = d.sample(frac=1)

        #split training and testing data
        d_train= d[:self.max_train_line]
        d_test = d[self.max_train_line:]

        d_train_att = d_train.drop(['pass'], axis=1)
        d_train_pass = d_train['pass']

        d_test_att = d_test.drop(['pass'], axis=1)
        d_test_pass = d_test['pass']

        d_att = d.drop(['pass'], axis=1)
        d_pass = d['pass']

