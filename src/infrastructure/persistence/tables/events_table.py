from sqlalchemy import JSON, Boolean, Column, Integer, String, Table

from infrastructure.persistence.database import SQLALCHEMY_MAPPER_REGISTRY

events_table = Table(
    "events",
    SQLALCHEMY_MAPPER_REGISTRY.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("uuid", String(36), unique=True, nullable=False, index=True),
    Column("event_type", String(255), nullable=False),
    Column("payload", JSON, nullable=False),
    Column("is_processed", Boolean, nullable=False),
    schema="public",
)
