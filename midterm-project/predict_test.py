import requests
import pandas as pd
import json


url = 'http://localhost:9696/predict'

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

json_resultante = mrnaData.iloc[1000, :].to_json()

json_cargado = json.loads(json_resultante)

# Convertir las claves a tipo numérico
customer = {int(k): v for k, v in json_cargado.items()}

							
response = requests.post(url, json=customer).json() # .json() converts the response to JSON
print(response)

if response['cancer_class'] == 1:
    print('Yes cancer')
else:
    print('No cancer')