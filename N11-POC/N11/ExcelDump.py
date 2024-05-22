import  pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['N11']
collection = db['Amazon']
cusor = collection.find({} , {'_id': False})
print(type(cusor))

df = pd.DataFrame(cusor )
df.to_excel('Amazon.xlsx' , index=False)
print(df)
