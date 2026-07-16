from fastapi import APIRouter, Depends

from app.customers.application.use_cases.list_customers import ListCustomersUseCase
from app.customers.presentation.schemas.customer_schema import CustomerResponse
from app.customers.presentation.dependencies.customer_dependencies import (
    get_list_customers_use_case,
)
from app.customers.presentation.schemas.customer_schema import (
    CustomerCreate,
    CustomerResponse,
)
from app.customers.application.use_cases.create_customer import (
    CreateCustomerUseCase,
)

from app.customers.presentation.dependencies.customer_dependencies import (
    get_create_customer_use_case,
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

@router.post(
    "",
    response_model=CustomerResponse,
    status_code=201,
)
def create_customer(
    customer: CustomerCreate,
    use_case: CreateCustomerUseCase = Depends(
        get_create_customer_use_case
    ),
):

    return use_case.execute(
        name=customer.name,
        email=customer.email,
    )