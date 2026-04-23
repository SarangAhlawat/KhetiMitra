from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys
import os
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.core.rate_limiter import limiter

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )
)

# Create FastAPI app
app = FastAPI(
    title="AI DSS Sustainable Farming API",
    description="""
    AI-Powered Decision Support System
    for Sustainable Farming.

    Features:
    - Crop Recommendation
    - QSSM Sustainability Score
    - Environmental Intelligence
    - Voice-based Advisory
    - Government Scheme Matching
    """,
    version="1.0.0",

)


from app.core.logging_middleware import logging_middleware

app.middleware("http")(logging_middleware)

from app.core.error_middleware import (
    error_handling_middleware
)

app.middleware("http")(
    error_handling_middleware
)


from fastapi.responses import JSONResponse


@app.exception_handler(RateLimitExceeded)

async def rate_limit_handler(
    request,
    exc
):

    return JSONResponse(

        status_code=429,

        content={
            "success": False,
            "error": "Rate limit exceeded"
        }

    )


# Import routers
from app.api import qssm_routes

# Register routers
app.include_router(
    qssm_routes.router,
    # prefix="/qssm",
    # tags=["QSSM"]
)


# Root test route
@app.get("/")
def root():
    return {
        "message": "AI DSS API Running"
    }


from app.api.knowledge_routes import router as knowledge_router

app.include_router(
    knowledge_router,
    prefix="/knowledge",
    tags=["Knowledge"]
)

# from fastapi import FastAPI

from app.api import (
    farmer_routes,
    farm_routes,
    environment_routes,
    recommendation_routes
)


# app = FastAPI()


app.include_router(
    farmer_routes.router
)

app.include_router(
    farm_routes.router
)

app.include_router(
    environment_routes.router
)

app.include_router(
    recommendation_routes.router
)

from app.api import history_routes


app.include_router(
    history_routes.router
)


from app.api import auth_routes


app.include_router(
    auth_routes.router
)

from app.api import voice_routes


app.include_router(
    voice_routes.router
)



app.state.limiter = limiter

app.add_middleware(
    SlowAPIMiddleware
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)