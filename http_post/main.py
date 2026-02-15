from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Define a request body model
class UserInfo(BaseModel):
    name: str
    age: int
    gender: str

@app.post("/userinfo")
def create_userinfo(user: UserInfo):
    # Print to server console
    print(f"Name: {user.name}, Age: {user.age}, Gender: {user.gender}")
    
    # Return JSON response
    return {
        "message": f"Hello {user.name}!",
        "age": user.age,
        "gender": user.gender
    }

if __name__ == "__main__": 
    uvicorn.run(app, host="127.0.0.1", port=8000)
# iwr http://127.0.0.1:8000/userinfo -Method POST -Body '{"name":"Wasan","age":25,"gender":"Female"}' -ContentType "application/json"