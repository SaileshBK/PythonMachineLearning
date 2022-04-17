import pandas as pnd
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier
import joblib

#visualazing the tree model
#from sklearn import tree


# movies_data = pnd.read_csv('movies.csv')
# X = movies_data.drop(columns=['type'])  
# y = movies_data['type']

# testing accuracy of the model

# #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)
# #model = DecisionTreeClassifier()
# #model.fit(X_train,y_train)
# #predictions = model.predict(X_test)

# myScore = accuracy_score(y_test,predictions)
# print(myScore)

# Now, Model persistant

# model = DecisionTreeClassifier()
# model.fit(X,y)
#joblib.dump(model,'movie-type.joblib')



# now loading the model
model = joblib.load('movie-type.joblib')
#example, Age 21 female
predictions = model.predict([[21,1]])
print(predictions)



# for visualazing the tree model
# movies_data = pnd.read_csv('movies.csv')
# X = movies_data.drop(columns=['type'])  
# y = movies_data['type']
# model = DecisionTreeClassifier()
# model.fit(X,y)

# tree.export_graphviz(model, out_file='movies-type.dot',feature_names=['age','gender'],class_names=sorted(y.unique()),
# label='all',rounded=True,filled=True)
