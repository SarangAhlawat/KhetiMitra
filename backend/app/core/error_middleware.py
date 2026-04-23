from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import get_logger


logger = get_logger(__name__)


async def error_handling_middleware(
    request: Request,
    call_next
):

    try:

        response = await call_next(request)

        return response

    except Exception as e:

        logger.error(
            f"Unhandled Error | {str(e)}"
        )

        return JSONResponse(

            status_code=500,

            content={
                "success": False,
                "error": "Internal Server Error"
            }

        )