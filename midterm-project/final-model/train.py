import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

# Parameters

max_depth = 2
min_samples_leaf = 20

output_file = 'final_model.bin'

#Data preparation

DATA_PATH = '../data/BRCA.rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes_normalized__data.data.txt'
mrnaNorm = pd.read_csv(DATA_PATH, header=None, sep='\t', skiprows=2)
mrnaIDs = pd.read_csv(DATA_PATH, header=None, sep='\t', nrows=1)
mrnaIDs = mrnaIDs.iloc[:, 1:].iloc[0]

# Create 'mrnaClass' and 'mrnaClassNum'
samp = [t.split("-")[3][:2] for t in mrnaIDs]
sampleType = pd.DataFrame(samp)
sampClass = [1 if int(t) < 10 else 0 for t in samp]
mrnaClass = pd.DataFrame(sampClass)

sampClassNum = [1 if int(t) < 10 else 0 for t in samp]
mrnaClassNum = pd.DataFrame(sampClassNum)

# Create 'geneNames'
geneNames = mrnaNorm.iloc[:, 0]

# Transpose 'mrnaNorm'
mrnaData = mrnaNorm.iloc[:, 1:].T

mrnaData_full_train, mrnaData_test, mrnaClassNum_full_train, mrnaClassNum_test = train_test_split(
    mrnaData, mrnaClassNum, test_size=0.2, random_state=1, stratify=mrnaClassNum
)


# Restablecer los índices
df_train = mrnaData_full_train.reset_index(drop=True)
df_test = mrnaData_test.reset_index(drop=True)

# Las variables objetivo
y_train = mrnaClassNum_full_train.values.ravel()
y_test = mrnaClassNum_test.values.ravel()

# Training

def train(df_train, y_train, max_depth=max_depth, min_samples_leaf=min_samples_leaf):
    dicts = df_train.to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df.to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# Training the final model
print('training the final model')

dv, model = train(df_train, y_train, max_depth, min_samples_leaf)
y_pred = predict(df_test, dv, model)


auc = roc_auc_score(y_test, y_pred)

print('AUC: %.3f' % auc)

# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)

print('Model saved to %s' % output_file)