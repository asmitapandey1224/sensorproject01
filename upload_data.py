from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
uri = "mongodb+srv://asmitapandey1224:9WOMaEpnsX0fB9Zb@cluster0.vhxf9o1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv(r"C:\Users\asmit\OneDrive\Desktop\Sensor_fault\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis = 1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)