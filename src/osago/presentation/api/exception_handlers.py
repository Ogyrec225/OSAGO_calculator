import traceback
from dataclasses import asdict

from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger

from osago.domain.base_exceptions import ApplicationError, DomainError
from osago.presentation.api.responses.base import ErrorData, ErrorResponse


async def generic_exception_handler(
    request: Request, exc: DomainError | ApplicationError
) -> JSONResponse:
    error_data = ErrorData(type=exc.type, detail=exc.title)

    error_response = ErrorResponse(status=False, error=error_data)

    logger.opt(depth=11).error(f"[{exc.type}] - {exc.title}")

    response_content = asdict(error_response)

    return JSONResponse(status_code=exc.status, content=response_content)


async def internal_server_error_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    error_data = ErrorData(
        type="InternalServerError", detail="Произошла непредвиденная ошибка."
    )
    error_response = ErrorResponse(status=False, error=error_data)

    full_traceback = traceback.format_exc()
    logger.critical(
        f"Unexpected ERROR: {exc}\n{full_traceback}", full_traceback=full_traceback
    )

    return JSONResponse(status_code=500, content=asdict(error_response))
