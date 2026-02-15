from fastapi import FastAPI, Query
import uvicorn

# Create FastAPI app instance
app = FastAPI()

@app.get("/greet")
def greet_user(name: str = Query(..., min_length=1, max_length=50)):
  
    # Print the name to the server console
    print(f"Received name: {name}")

    # Return a JSON response
    return {"message": f"Hello, {name}!"}

    #http://127.0.0.1:8000/greet?name=Wasan


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)
