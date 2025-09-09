from fastapi import FastAPI 
from dotenv import load_dotenv #before the base read it
load_dotenv(".env")

from routes import base #base.py


app=FastAPI()
app.include_router(base.base_router)