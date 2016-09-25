# Save basic ML model using pickle
import pandas as pd
from sklearn import cross_validation
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import pickle
from test_all_indices import run_all_tests

names = ['coherence', 'determinants', 'phrase_len', 'time', 'self',
        'surveillance', 'unfair', 'mind_control', 'alien']

df2 = pd.DataFrame(data=run_all_tests(), index=names)
df = df2.transpose()

df['type'] = ["Schizophrenia","Schizophrenia","Schizophrenia","Schizophrenia",
 "Schizophrenia","Schizophrenia","Schizophrenia","Schizophrenia",
 "Control","Control","Control","Control","Control","Control","Control",
 "Control","Control","Control","Control","Control","Control","Control",
 "Control","Control","Control","Control",
 "Control","Control","Control","Control"]

print(df)

array = df.values

X = array[:,0:9]
Y = array[:,9]

test_size = 0.33
seed = 3
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on 33%
model = LogisticRegression()
model.fit(X, Y)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X, Y)
print(result)
