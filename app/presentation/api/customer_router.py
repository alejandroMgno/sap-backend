from fastapi import APIRouter, Depends

from app.application.use_cases.list_customers import ListCustomersUseCase
from app.presentation.dependencies.customer_dependencies import (
    get_list_customers_use_case,
)


router = APIRouter(
    prefix="/api/v1/customers",
    tags=["Customers"],
)


@router.get("")
def list_customers(
    use_case: ListCustomersUseCase = Depends(
        get_list_customers_use_case
    ),
):

    customers = use_case.execute()

    return customers