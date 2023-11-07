from domain.entities.user_entity import UserEntity
from infrastructure.persistence.repositories.abstract_repository import (
    AbstractSQLAlchemyRepository,
)


class UserRepository(AbstractSQLAlchemyRepository[UserEntity]):
    @property
    def _entity_class(self):
        return UserEntity
