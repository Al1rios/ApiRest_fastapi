from fastapi import APIRouter



router = APIRouter(prefix="/manage_payables_receivables")

@router.get("/")
def list_all_payables_and_receivables():
    return [{
        "contas1":"contas1"
    },{
        "contas2":"contas2"
    }]