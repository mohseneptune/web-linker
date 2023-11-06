from abc import abstractmethod
from typing import Generic, Optional, TypeVar

from sqlalchemy.orm import Session

from domain.entities.base_entity import BaseEntity
from domain.repository import AbstractRepository

BaseEntityT = TypeVar("BaseEntityT", bound=BaseEntity)


class AbstractSQLAlchemyRepository(AbstractRepository, Generic[BaseEntityT]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def _add(self, entity: BaseEntityT) -> None:
        self.session.add(entity)

    def _get(self, entity_id: int) -> Optional[BaseEntityT]:
        return self.session.query(self._entity_class).get(entity_id)

    @property
    @abstractmethod
    def _entity_class(self):
        """
        The SQLAlchemy model class that the repository is responsible for.
        This should be defined in the concrete repository subclass.
        """
        raise NotImplementedError
