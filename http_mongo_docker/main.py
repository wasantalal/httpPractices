from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017")
db = client["Task4"]
users_col = db["Day1"]

@app.get("/user/{name}")
def get_user(name: str):
    # Find the user in the database
    user = users_col.find_one({"name": name}, {"_id": 0}) 
    
    if user:
        return user
    return {"error": "User not found"}

    #http://127.0.0.1:8000/user/Wasan

if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)


