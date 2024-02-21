import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
