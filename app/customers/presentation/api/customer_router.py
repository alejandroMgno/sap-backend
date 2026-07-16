from fastapi import APIRouter, Depends

from app.customers.application.use_cases.list_customers import ListCustomersUseCase
from app.customers.presentation.schemas.customer_schema import CustomerResponse
from app.customers.presentation.dependencies.customer_dependencies import (
    get_list_customers_use_case,
)


router = APIRouter(
    prefix="/api/v1/customers",
    tags=["Customers"],
)


@router.get(
    "",
    response_model=list[CustomerResponse],
)
def list_customers(
    use_case: ListCustomersUseCase = Depends(
        get_list_customers_use_case
    ),
):

    customers = use_case.execute()

    return customers