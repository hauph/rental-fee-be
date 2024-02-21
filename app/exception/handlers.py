from starlette.requests import Request
from starlette.responses import JSONResponse

from app.exception.exceptions import ValidationException


async def validation_error_handler(
    request: Request, exception: ValidationException
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": exception.message},
    )


exception_handlers = {ValidationException: validation_error_handler}
