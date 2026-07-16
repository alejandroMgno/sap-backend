from app.customers.infrastructure.container.container import Container
from app.customers.application.use_cases.create_customer import (
    CreateCustomerUseCase,
)
from app.customers.infrastructure.repositories.memory_customer_repository import MemoryCustomerRepository


def get_list_customers_use_case():

    return Container.list_customers_use_case()

def get_create_customer_use_case():

    repository = MemoryCustomerRepository()

    return CreateCustomerUseCase(repository)