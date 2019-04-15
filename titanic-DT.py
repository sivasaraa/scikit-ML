import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split

df = pd.read_csv("sampletitanic.csv")

input = df.drop(['PassengerId','Survived','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis="columns")
target = df['Survived']

le_sex = LabelEncoder()

input['sex_n'] = le_sex.fit_transform(input['Sex'])
input_n = input.drop('Sex',axis="columns")
input_n.fillna(input_n['Age'].mean(),inplace=True)

x_train,x_test,y_train,y_test = train_test_split(input_n,target,test_size=0.2)

model = tree.DecisionTreeClassifier()
model.fit(x_train,y_train)

print(model.score(x_test,y_test))

print(model.predict(x_test))
