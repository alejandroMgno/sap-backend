from pydantic import BaseModel,EmailStr,Field

class CustomerCreate(BaseModel):
    name: str = Field(
        min_length=30,
        max_length=100,
        example="Juan Pérez",
    )
    email: EmailStr 

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

