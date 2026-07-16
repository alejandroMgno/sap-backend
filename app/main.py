from fastapi import FastAPI
from app.presentation.api.home_router import router as home_router
from app.shared.constats import APP_NAME, APP_VERSION, APP_DESCRIPTION
from app.presentation.api.customer_router import router as customer_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)

app.include_router(home_router)
app.include_router(customer_router)