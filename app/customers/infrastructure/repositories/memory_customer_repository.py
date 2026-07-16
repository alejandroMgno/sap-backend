from app.customers.domain.entities.customer import Customer
from app.customers.domain.repositories.customer_repository import CustomerRepository


class MemoryCustomerRepository(CustomerRepository):

    def __init__(self):

        self.customers = [
            Customer(
                id=1,
                name="Juan Pérez",
                email="juan@example.com",
            ),
            Customer(
                id=2,
                name="María López",
                email="maria@example.com",
            ),
            Customer(
                id=3,
                name="Carlos Ruiz",
                email="carlos@example.com",
            ),
        ]

    def get_all(self) -> list[Customer]:
        return self.customers

    def get_by_email(
        self,
        email: str,
    ) -> Customer | None:

        for customer in self.customers:

            if customer.email == email:
                return customer

        return None

    def create(
        self,
        customer: Customer,
)       -> Customer:

        next_id = max(
        customer.id
        for customer in self.customers
        ) + 1

        customer.id = next_id

        self.customers.append(customer)

        return customer 