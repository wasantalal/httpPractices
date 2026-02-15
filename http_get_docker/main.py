from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# Create FastAPI app instance
app = FastAPI()

@app.get("/name")
def get_name():
    
    greeting = {"message": "Hello Wassan"}
    return JSONResponse(content=greeting, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)