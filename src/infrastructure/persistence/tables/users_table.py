from sqlalchemy import Column, Integer, String, Table

from infrastructure.persistence.database import SQLALCHEMY_MAPPER_REGISTRY

users_table = Table(
    "users",
    SQLALCHEMY_MAPPER_REGISTRY.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("uuid", String(36), unique=True, nullable=False, index=True),
    Column("username", String(255), unique=True, nullable=False),
    Column("hashed_password", String(255), nullable=False),
    Column("first_name", String(50), nullable=True),
    Column("last_name", String(50), nullable=True),
    schema="accounts",
)
