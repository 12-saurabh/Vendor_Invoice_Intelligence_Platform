from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.crud.prediction import (
    get_all_predictions,
    get_prediction_by_invoice,
)

from app.schemas.prediction import PredictionResponse


router = APIRouter(
    prefix="/prediction",
    tags=["ML Prediction"],
)


@router.get(
    "/",
    response_model=List[PredictionResponse],
)
def get_predictions(
    db: Session = Depends(get_db),
):
    return get_all_predictions(db)


@router.get(
    "/{invoice_id}",
    response_model=PredictionResponse,
)
def get_prediction(
    invoice_id: int,
    db: Session = Depends(get_db),
):

    prediction = get_prediction_by_invoice(
        db,
        invoice_id,
    )

    if prediction is None:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found",
        )

    return prediction