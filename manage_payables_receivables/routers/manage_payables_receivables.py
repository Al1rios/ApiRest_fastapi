from decimal import Decimal
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/manage_payables_receivables")

class ManagePayablesReceivablesResponse(BaseModel):
    id: int
    description: str
    value: Decimal
    type: str # payables, receivables

class ManagePayablesReceivablesRequest(BaseModel):
    description: str
    value: Decimal
    type: str # payables, receivables

@router.get("/", response_model=List[ManagePayablesReceivablesResponse])
def list_all_payables_and_receivables():
    return [
        ManagePayablesReceivablesResponse(
            id = 1,
            description = "rent",
            value = 2300.50,
            type = "payables"
        ),
        ManagePayablesReceivablesResponse(
            id=2,
            description="salary",
            value=5000.90,
            type="receivables"
        ),
    ]


@router.post("/", response_model=ManagePayablesReceivablesResponse, status_code=201)
def create_account(account: ManagePayablesReceivablesRequest):
    return ManagePayablesReceivablesResponse(
            id=3,
            description=account.description,
            value=account.value,
            type=account.type
        )