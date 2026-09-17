from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.db import Base
from app.db.session import SessionLocal, engine
import app.models  # noqa: F401  Ensures every SQLAlchemy model is registered.
from app.services.user_service import create_demo_admin


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")

    @app.on_event("startup")
    def initialize_database() -> None:
        Base.metadata.create_all(bind=engine)
        with SessionLocal() as db:
            create_demo_admin(db)

    return app


app = create_app()
