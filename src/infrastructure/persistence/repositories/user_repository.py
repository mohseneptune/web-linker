from domain.entities.user_entity import UserEntity

from .abstract_sqlalchemy_repository import AbstractSQLAlchemyRepository


class UserRepository(AbstractSQLAlchemyRepository[UserEntity]):
    @property
    def _entity_class(self):
        return UserEntity
