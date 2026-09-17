from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User

DEMO_ADMIN_USERNAME = "admin"
DEMO_ADMIN_PASSWORD = "Admin123!"


def create_demo_admin(db: Session) -> User:
    user = db.scalar(select(User).where(User.username == DEMO_ADMIN_USERNAME))
    if user is None:
        user = User(
            username=DEMO_ADMIN_USERNAME,
            password_hash=hash_password(DEMO_ADMIN_PASSWORD),
            display_name="系统管理员",
            role="admin",
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user
