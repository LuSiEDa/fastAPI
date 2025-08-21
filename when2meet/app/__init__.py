from fastapi import FastAPI
from app.configs.tortoise_config import initialize_tortoise


app = FastAPI()
initialize_tortoise(app)
