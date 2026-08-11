from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from app.core.configuration import settings


DB_URL=f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

class BaseModel(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)