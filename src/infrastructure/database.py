from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from settings import POSTGRES_DATABASE_URI

SQLALCHEMY_MAPPER_REGISTRY = registry()

POSTGRES_ENGIN = create_engine(POSTGRES_DATABASE_URI)

POSTGRES_SESSION_FACTORY = sessionmaker(
    autocommit=False, autoflush=False, bind=POSTGRES_ENGIN
)
