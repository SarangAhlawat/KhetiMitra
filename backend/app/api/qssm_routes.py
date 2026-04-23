from fastapi import APIRouter
import pandas as pd

from app.services.qssm_service import compute_qssm

router = APIRouter()


@router.post("/compute-qssm")

def compute():

    df = pd.read_csv(
        "../data/processed/dataset_with_qssm.csv"
    )

    df = compute_qssm(df)

    return {

        "status": "QSSM Computed"

    }