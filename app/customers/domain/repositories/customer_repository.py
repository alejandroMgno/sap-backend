from abc import ABC, abstractmethod

from app.customers.domain.entities.customer import Customer


class CustomerRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Customer]:
        pass