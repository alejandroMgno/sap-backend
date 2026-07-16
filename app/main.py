from fastapi import FastAPI
from app.customers.presentation.api.home_router import router as home_router
from shared.constats import APP_NAME, APP_VERSION, APP_DESCRIPTION
from app.customers.presentation.api.customer_router import router as customer_router
from shared.handlers.exception_handler import (
    customer_already_exists_handler,
)

from shared.exceptions.exception import (
    CustomerAlreadyExistsError,
)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)

app.include_router(home_router)
app.include_router(customer_router)
app.add_exception_handler(
    CustomerAlreadyExistsError,
    customer_already_exists_handler,
)