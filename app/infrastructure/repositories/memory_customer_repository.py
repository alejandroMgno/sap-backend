from app.domain.entities.customer import Customer
from app.domain.repositories.customer_repository import CustomerRepository


class MemoryCustomerRepository(CustomerRepository):

    def get_all(self) -> list[Customer]:
        return [
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