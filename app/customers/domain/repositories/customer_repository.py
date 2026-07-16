from abc import ABC, abstractmethod

from app.customers.domain.entities.customer import Customer


class CustomerRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Customer]:
        pass

    @abstractmethod
    def get_by_email(
        self,
        email: str,
    ) -> Customer | None:
        pass

    @abstractmethod
    def create(
        self,
        customer: Customer,
    ) -> Customer:
        pass