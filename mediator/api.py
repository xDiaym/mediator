import sys
from typing import List

from fastapi import APIRouter
from loguru import logger

from mediator.models import Batch, Threshold, Prediction, Model
from mediator.predictor import Predictor

logger.add(
    "mediator.log",
    format="[{level}] {time}: {message}",
    level="INFO",
    rotation="32 MB"
)
predictor = Predictor()
router = APIRouter(prefix="/v1")


@router.get("/model", response_model=Model)
async def get_model():
    return Model(kind=predictor.get_model_kind())


@router.post("/model")
async def set_model(model: Model):
    logger.info("model changed to {}", model.kind)
    predictor.set_model(model.kind)
    return {"ok": True}


@router.get("/threshold", response_model=Threshold)
def get_threshold():
    return {"threshold": predictor.threshold}


@router.post("/threshold")
def set_threshold(body: Threshold):
    logger.info("threshold changed to {}", body.threshold)
    predictor.threshold = body.threshold
    return {"ok": True}


@router.post("/predict", response_model=List[Prediction])
async def predict(batch: Batch):
    texts, payloads = batch.split()
    predictions = predictor.predict(texts)
    return [
        Prediction(is_aggressive=pred, payload=pl)
        for pred, pl in zip(predictions, payloads)
    ]
