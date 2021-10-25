import pandas as pd

#load dataset of student portuguese scores
d = pd.read_csv('dataset/student-mat.csv', sep=';')

# generate binary label (pass/fail) based on G1+G2+G3 (test grades, each 0-20 pts); threshold for passing is sum>=30
d['pass'] = d.apply(lambda row: 1 if(row['G1'] + row['G2']+ row['G3']) >= 35 else 0, axis=1)

print(len(d))

# #drop periods marks column
# d = d.drop(['G1', 'G2', 'G3'], axis=1)

# #one-hot encoding on categorical columns
# d = pd.get_dummies(d, columns=['sex', 'school', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
#                                'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
#                                'nursery', 'higher', 'internet', 'romantic'])

# #shuffle rows
# d = d.sample(frac=1)

# #split training and testing data
# d_train= d[:500]
# d_test = d[500:]

# d_train_att = d_train.drop(['pass'], axis=1)
# d_train_pass = d_train['pass']

# d_test_att = d_test.drop(['pass'], axis=1)
# d_test_pass = d_test['pass']

# d_att = d.drop(['pass'], axis=1)
# d_pass = d['pass']

# #number of passing students in whole dataset:
# import numpy as np
# #print("Passing: %d out of %d (%.2f%%)" % (np.sum(d_pass), len(d_pass), 100*float(np.sum(d_pass)) / len(d_pass)))

# #fit a decision tree of max depth 5
# from sklearn import tree
# t = tree.DecisionTreeClassifier(criterion="entropy", max_depth=5)
# t = t.fit(d_train_att, d_train_pass)

# # save tree
# tree.export_graphviz(t, out_file="student-performance.dot", label="all", impurity=False,
#                     proportion=True, feature_names=list(d_train_att), class_names=["fail","pass"],
#                     filled=True, rounded=True)

# # check the tree score on test dataset
# print(t.score(d_test_att, d_test_pass))


# ##############Check the tree model accuracy for most depth (by example in range 1 to 19)
# # from sklearn.model_selection import cross_val_score

# # #scores = cross_val_score(t, d_att, d_pass, cv=5)
# # #show average score and +/- two standard deviations away (covering 95% of scores)
# # #print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))

# # # for max_depth in range(1,20):
# # #     t = tree.DecisionTreeClassifier(criterion="entropy", max_depth=max_depth)
# # #     scores = cross_val_score(t, d_att, d_pass, cv=5)
# # #     #show average score and +/- two standard deviations away (covering 95% of scores) of each max depth
# # #     print("Max depth: %d, Accuracy: %0.2f (+/- %0.2f)" % (max_depth, scores.mean(), scores.std()*2))


# # depth_acc = np.empty((19, 3), float)
# # i = 0
# # for max_depth in range(1,20):
# #     t = tree.DecisionTreeClassifier(criterion="entropy", max_depth=max_depth)
# #     scores = cross_val_score(t, d_att, d_pass, cv=5)
# #     depth_acc[i, 0] = max_depth
# #     depth_acc[i, 1] = scores.mean()
# #     depth_acc[i, 2] = scores.std()*2
# #     i+=1
# # # print(depth_acc)

# # import matplotlib.pyplot as plt
# # fig, ax = plt.subplots()
# # ax.errorbar(depth_acc[:,0], depth_acc[:,1], yerr=depth_acc[:,2])
# # ax.set_xlabel("Tree depth")
# # ax.set_ylabel("Tree accuracy")
# # ax.set_title("Tree accuracy according to depth")
# # plt.show()

# #CONclusion: Plus de  profondeur ne donne pas plus de précision


