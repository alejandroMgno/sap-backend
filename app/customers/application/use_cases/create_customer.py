from app.customers.domain.entities.customer import Customer
from app.customers.domain.repositories.customer_repository import CustomerRepository
from shared.exceptions.exception import CustomerAlreadyExistsError


class CreateCustomerUseCase:

#obtener el repositorio de clientes y asignarlo a la variable de instancia
    def __init__(
        self,
        repository: CustomerRepository,
    ):
        self.repository = repository
#busca un cliente existente por correo electrónico y lanza una excepción si ya existe, de lo contrario crea un nuevo cliente y lo guarda en el repositorio
    def execute(
        self,
        name: str,
        email: str,
    ) -> Customer:

        existing_customer = self.repository.get_by_email(email)

        if existing_customer:
            raise CustomerAlreadyExistsError(
                f"Customer with email '{email}' already exists."
            )
#aqui se crea un nuevo objeto Customer con los datos proporcionados y se llama al método create del repositorio para guardarlo
        customer = Customer(
            id=0,
            name=name,
            email=email,
        )
#retorna el cliente creado
        return self.repository.create(customer)