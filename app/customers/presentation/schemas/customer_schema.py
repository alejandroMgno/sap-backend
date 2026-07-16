from pydantic import BaseModel


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None = None