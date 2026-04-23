import time

from fastapi import Request

from app.core.logger import get_logger


logger = get_logger(__name__)


async def logging_middleware(
    request: Request,
    call_next
):

    start_time = time.time()

    # Log request

    logger.info(
        f"Request Started | {request.method} {request.url}"
    )

    try:

        response = await call_next(request)

    except Exception as e:

        logger.error(
            f"Request Failed | {str(e)}"
        )
        raise e

    process_time = time.time() - start_time

    logger.info(
        f"Request Completed | "
        f"{request.method} {request.url} | "
        f"Status {response.status_code} | "
        f"{process_time:.4f}s"
    )

    return response