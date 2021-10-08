from typing import List

from fastapi import APIRouter

from mediator.models import Batch, Threshold, Prediction, Model
from mediator.predictor import Predictor

predictor = Predictor()
router = APIRouter(prefix="/v1")


@router.get("/model", response_model=Model)
async def get_model():
    return Model(kind=predictor.get_model_kind())


@router.post("/model")
async def set_model(model: Model):
    print(model)
    predictor.set_model(model.kind)
    return {"ok": True}


@router.get("/threshold", response_model=Threshold)
def get_threshold():
    return {"threshold": predictor.threshold}


@router.post("/threshold")
def set_threshold(body: Threshold):
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
