from app.application.use_cases.list_customers import ListCustomersUseCase
from app.infrastructure.repositories.memory_customer_repository import (
    MemoryCustomerRepository,
)


def get_list_customers_use_case():

    repository = MemoryCustomerRepository()

    return ListCustomersUseCase(repository)