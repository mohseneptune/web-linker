from domain.entities.event_entity import EventEntity
from domain.entities.user_entity import UserEntity
from infrastructure.persistence.database import SQLALCHEMY_MAPPER_REGISTRY
from infrastructure.persistence.tables.events_table import events_table
from infrastructure.persistence.tables.users_table import users_table


def start_mappers():
    SQLALCHEMY_MAPPER_REGISTRY.map_imperatively(UserEntity, users_table)
    SQLALCHEMY_MAPPER_REGISTRY.map_imperatively(EventEntity, events_table)
