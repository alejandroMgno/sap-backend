from app.customers.application.use_cases.list_customers import ListCustomersUseCase

from app.customers.infrastructure.repositories.memory_customer_repository import (
    MemoryCustomerRepository,
)


class Container:

    @staticmethod
    def list_customers_use_case():

        repository = MemoryCustomerRepository()

        return ListCustomersUseCase(repository)