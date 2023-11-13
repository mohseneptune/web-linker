from abc import ABC, abstractmethod
from typing import Generic, Set, TypeVar

from domain.entities.base_entity import BaseEntity

BaseEntityT = TypeVar("BaseEntityT", bound=BaseEntity)


class AbstractRepository(ABC, Generic[BaseEntityT]):
    seen: Set[BaseEntityT]

    def __init__(self) -> None:
        self.seen = set()

    def add(self, entity: BaseEntityT) -> None:
        self._add(entity)
        self.seen.add(entity)

    def get(self, entity_id: int) -> BaseEntityT:
        return self._get(entity_id)

    @abstractmethod
    def _add(self, entity: BaseEntityT) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get(self, entity_id: int) -> BaseEntityT:
        raise NotImplementedError
