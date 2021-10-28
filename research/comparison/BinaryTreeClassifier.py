import pandas as pd
import numpy as np
from sklearn import tree
import os



class Performer:
    base_dir = './dataset'
    #according to investigations
    #by default we use portuguese course dataset
    #use 5 for binary tree best max_depth for portuguese course performance
    max_depth=5
    #use 500 for rows lines shuffled for training (60% of dataset) 
    max_train_line=500
    
    #load dataset of student portuguese scores
    d1 = pd.read_csv(os.path.join(base_dir,'student-por.csv'), sep=';')
    d2 = pd.read_csv(os.path.join(base_dir,'student-mat.csv'), sep=';')
    d = pd.concat([d1, d2])
    is_trained=False


    def __init__(self):
        # if course=='mat':
        #     self.d = pd.read_csv(os.path.join(self.base_dir,'dataset/student-mat.csv'), sep=';')
        #     #use 11 for binary tree best max_depth for math course performance
        #     self.max_depth=11
        #     #use 200 for rows lines shuffled for training (60% of dataset) 
        #     self.max_train_line=200

        #generate binary label (pass/fail) based on G1+G2+G3 (test grades, each 0-20 pts); threshold for passing is sum>=30
        self.d['pass'] = self.d.apply(lambda row: 1 if(row['G1'] + row['G2']+ row['G3']) >= 35 else 0, axis=1)

        #drop periods marks column
        self.d = self.d.drop(['G1', 'G2', 'G3'], axis=1)

        #one-hot encoding on categorical columns
        self.d = pd.get_dummies(self.d, columns=['sex', 'school', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
                                    'nursery', 'higher', 'internet', 'romantic'])

        #shuffle rows
        self.d = self.d.sample(frac=1)
        self.d_train= self.d[:self.max_train_line]
        self.d_test = self.d[self.max_train_line:]
        self.d_att = self.d.drop(['pass'], axis=1)

        

        

    def train(self):
        #split training data
        self.d_train_att = self.d_train.drop(['pass'], axis=1)
        self.d_train_pass = self.d_train['pass']

        #build binary tree classifier
        self.tree_classifier = tree.DecisionTreeClassifier(criterion="entropy", max_depth=self.max_depth)
        #train it on training data
        self.tree_classifier = self.tree_classifier.fit(self.d_train_att, self.d_train_pass)

        self.is_trained=True

        


    def test_model(self):
        #split testing data
        d_test_att = self.d_test.drop(['pass'], axis=1)
        d_test_pass = self.d_test['pass']

        #if tree not trained then train it
        if not self.is_trained:
            self.train()
        
        # show the tree score on test dataset
        print(self.tree_classifier.score(d_test_att, d_test_pass))



    def evaluate_student(self, data):
        return self.tree_classifier.predict(data[self.d_att.columns])
