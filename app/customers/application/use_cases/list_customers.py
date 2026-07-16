from app.customers.domain.repositories.customer_repository import CustomerRepository


class ListCustomersUseCase:

    def __init__(
        self,
        repository: CustomerRepository,
    ):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()