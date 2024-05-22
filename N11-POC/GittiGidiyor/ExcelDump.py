import  pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['N11']
collection = db['Hepsiburada']
cusor = collection.find({} , {'_id': False})
print(type(cusor))

df = pd.DataFrame(cusor )
df.to_excel('GittiGidiyor.xlsx' , index=False)
print(df)
