from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """Provide a lightweight endpoint for deployment and frontend checks."""
    return {"status": "ok"}
