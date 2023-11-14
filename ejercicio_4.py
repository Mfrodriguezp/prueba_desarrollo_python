import requests
import json

url = "https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset"

def getEmployee ():
    peticion = requests.get(url)
    data = json.loads(peticion)

