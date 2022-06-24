from fastapi import FastAPI
from uvicorn

app = FastAPI

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)