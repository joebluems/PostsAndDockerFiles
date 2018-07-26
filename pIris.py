import pandas as pd
import sys
import json
import requests

if len(sys.argv)!=3:
  print("Usage: python",sys.argv[0]," <IP> <PORT>")
  sys.exit(0)

URL = "http://%s:%s/predict" % (sys.argv[1],sys.argv[2])

#### Setting the headers to send and accept json responses ####
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

#### Reading data & sampling then convert to JSON #### 
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv('./iris.csv', names=names)
df = df.sample(frac=0.1,replace=False, random_state=1)
data = df.to_json(orient='records')

if (sys.argv[2])=="5000":
  ##### KNN MODEL from Python ####
  resp = requests.post(URL, data = json.dumps(data),headers= header)
  print("Results from sklearn KNN model API...")
  x = resp.json()
  y=json.loads(x['predictions'])
  for item in y:
    print("KNN: %s		Actual: %s" % (item['KNN_result'],item['actual']))


elif (sys.argv[2])=="5001":
  ##### SVM MODEL from Python ####
  resp = requests.post(URL, data = json.dumps(data),headers= header)
  print("Results from sklearn SVM model API...")
  x = resp.json()
  y=json.loads(x['predictions'])
  for item in y:
    print("SVM: %s		Actual: %s" % (item['SVM_result'],item['actual']))


elif (sys.argv[2])=="5001":
  ##### SVM MODEL from Python ####
  resp = requests.post(URL, data = json.dumps(data),headers= header)
  print("Results from sklearn SVM model API...")
  x = resp.json()
  y=json.loads(x['predictions'])
  for item in y:
    print("SVM: %s		Actual: %s" % (item['SVM_result'],item['actual']))

elif (sys.argv[2])=="5002":
  URL = "http://%s:%s/iris_api" % (sys.argv[1],sys.argv[2])
  ##### RF MODEL from R  #########
  print("\nResults from Random Forest (R) model API...")
  for index, row in df.iterrows():
     d = '{"Sepal.Length":%.1f, "Sepal.Width":%.1f,"Petal.Length":%.1f,"Petal.Width":%.1f}' \
        % (row["sepal-length"],row["sepal-width"],row["petal-length"],row["petal-width"])
     resp = requests.post(URL, data = d,headers= header)
     print("RF:  %s               Actual:%s" % (resp.text,row['class']))

