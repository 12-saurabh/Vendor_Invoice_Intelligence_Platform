from sqlalchemy.orm import Session

from app.models.prediction import Prediction
from app.schemas.prediction import PredictionCreate


def create_prediction(
    db: Session,
    prediction: PredictionCreate
):

    db_prediction = Prediction(
        invoice_id=prediction.invoice_id,
        risk_score=prediction.risk_score,
        prediction=prediction.prediction,
        confidence=prediction.confidence
    )

    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)

    return db_prediction


def get_all_predictions(
    db: Session
):

    return db.query(Prediction).all()


def get_prediction_by_invoice(
    db: Session,
    invoice_id: int
):

    return (
        db.query(Prediction)
        .filter(Prediction.invoice_id == invoice_id)
        .first()
    )