import enum
from typing import List, Tuple, Any

from pydantic import Field
from pydantic.main import BaseModel


class Threshold(BaseModel):
    threshold: float = Field(0.5, ge=0, le=1)


class ModelKind(enum.Enum):
    FTSN = "ftsn"
    FTT = "ftt"


class Model(BaseModel):
    kind: ModelKind


class Message(BaseModel):
    text: str
    payload: Any


class Prediction(BaseModel):
    is_aggressive: bool
    payload: Any


class Batch(BaseModel):
    __root__: List[Message]

    def split(self) -> Tuple[List[str], List[Any]]:
        texts = list(map(lambda x: x.text, self.__root__))
        payloads = list(map(lambda x: x.payload, self.__root__))
        return texts, payloads
