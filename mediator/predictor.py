from typing import List, Union

from dostoevsky.models import (
    FastTextSocialNetworkModel,
    FastTextToxicModel,
)

# FastText Social Network, FastText Toxic
from dostoevsky.tokenization import RegexTokenizer

from mediator.models import ModelKind


class Predictor:
    _KIND_TO_MODEL_CLS = {
        ModelKind.FTSN: FastTextSocialNetworkModel,
        ModelKind.FTT: FastTextToxicModel,
    }

    def __init__(
        self, *, model: ModelKind = ModelKind.FTSN, threshold: float = 0.5
    ) -> None:
        self._threshold = threshold
        self._model = None
        self._model_kind = None
        self.set_model(model)

    @property
    def threshold(self) -> float:
        return self._threshold

    @threshold.setter
    def threshold(self, value: float) -> None:
        if not (0 <= value <= 1):
            raise ValueError("Threshold should be in [0; 1].")
        self._threshold = value

    def get_model_kind(self) -> ModelKind:
        return self._model_kind

    def set_model(self, model_kind: ModelKind) -> None:
        tokenizer = RegexTokenizer()
        model_cls = self._KIND_TO_MODEL_CLS[model_kind]
        self._model_kind = model_kind
        self._model = model_cls(tokenizer)

    def predict(self, texts: List[str]) -> List[bool]:
        predictions = self._model.predict(texts)
        results = map(
            lambda x: x.get("negative", 0) >= self._threshold, predictions
        )
        # Dostoevsky returns dict of numpy bool. Pydantic don't work with numpy.
        return list(map(bool, results))
