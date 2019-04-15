import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

df = pd.read_csv("salaries.csv")
print(df.head())

input = df.drop('salary_more_then_100k',axis=1)

target = df['salary_more_then_100k']

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

input['company_n'] = le_company.fit_transform(input['company'])
input['job_n'] = le_job.fit_transform(input['job'])
input['degree_n'] = le_degree.fit_transform(input['degree'])

input_n = input.drop(['company','job','degree'],axis='columns')

model = tree.DecisionTreeClassifier()
model.fit(input_n,target)
print(model.score(input_n,target))

result = model.predict([[0,0,2]])
print(result)