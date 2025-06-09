from fastapi import FastAPI
from reflex.backend import app as reflex_app

api = FastAPI()
api.mount("/", reflex_app)

app = api  # Vercel custom handler
