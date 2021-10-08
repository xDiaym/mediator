from fastapi import FastAPI

from mediator.api import router
from mediator.predictor import Predictor

predictor = Predictor()
app = FastAPI()

app.include_router(router)
