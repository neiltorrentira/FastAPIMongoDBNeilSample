from fastapi import FastAPI
from routes.User import user

app = FastAPI()
app.include_router(user)
