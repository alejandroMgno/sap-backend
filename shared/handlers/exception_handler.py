from fastapi import Request
from fastapi.responses import JSONResponse

from shared.exceptions.exception import (
    CustomerAlreadyExistsError,
)

#aqui se define un manejador de excepciones para la excepción CustomerAlreadyExistsError, que devuelve una respuesta JSON con un código de estado 409 y un mensaje de error detallado
async def customer_already_exists_handler(
    request: Request,
    exc: CustomerAlreadyExistsError,
):

    return JSONResponse(
        status_code=409,
        content={
            "detail": str(exc)
        },
    )