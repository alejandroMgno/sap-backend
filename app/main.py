from fastapi import FastAPI
from app.presentation.api.home_router import router as home_router
from app.shared.constats import APP_NAME, APP_VERSION, APP_DESCRIPTION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)

app.include_router(home_router)