from domain.entities.user_entity import UserEntity
from infrastructure.persistence.database import SQLALCHEMY_MAPPER_REGISTRY
from infrastructure.persistence.tables.users_table import users_table


def start_mappers():
    SQLALCHEMY_MAPPER_REGISTRY.map_imperatively(UserEntity, users_table)
