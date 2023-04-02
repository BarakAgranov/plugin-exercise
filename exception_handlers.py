from fastapi import FastAPI
from fastapi.responses import JSONResponse
from main import app
import logging

logger = logging.getLogger(__name__)


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logger.exception(exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )
