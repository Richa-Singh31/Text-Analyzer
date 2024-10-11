import subprocess
from fastapi import FastAPI
from app.endpoints import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    subprocess.Popen(["uvicorn", "main:app", "--reload"])
    subprocess.Popen(["streamlit", "run", "app.py"])