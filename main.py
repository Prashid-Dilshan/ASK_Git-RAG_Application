from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

app = FastAPI()



load_dotenv()  # Load environment variables from .env file

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") 




# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def greeting():
    return {"message": "Hello, World!"}

# Welcome endpoint
@app.get("/welcome")
def greeting2():
    return {"message": "Welcome to FastAPI!"}

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
