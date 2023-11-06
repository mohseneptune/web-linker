from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar

from domain.entities.base_entity import BaseEntity
from domain.repository import AbstractRepository

BaseEntityT = TypeVar("BaseEntityT", bound=BaseEntity)


class AbstractUnitOfWork(ABC, Generic[BaseEntityT]):
    """
    This abstract class represents the Unit of Work pattern which
    maintains a list of objects affected by a business transaction
    and coordinates the writing out of changes
    and the resolution of concurrency problems.

    Attributes:
        repositories (Dict[Type[BaseEntity], AbstractRepository]):
            A dictionary that maps entity types to their respective repositories.
    """

    repositories: Dict[Type[BaseEntityT], AbstractRepository[BaseEntityT]] = {}

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self) -> None:
        self._commit()

    @abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        """
        Rolls back the current transaction, discarding all changes made to the database.
        """
        raise NotImplementedError

    def register_repository(
        self,
        entity_type: Type[BaseEntityT],
        repository: AbstractRepository[BaseEntityT],
    ) -> None:
        """
        Registers a repository with the unit of work for a given entity type.

        entity_type (Type[BaseEntityT]):
        The entity type class for which the repository is being registered.

        repository (AbstractRepository[BaseEntityT]):
        The repository instance to be associated with the entity type.
        """
        self.repositories[entity_type] = repository

    def get_repository(
        self, entity_type: Type[BaseEntityT]
    ) -> AbstractRepository[BaseEntityT]:
        """
        Retrieves a registered repository for a given entity type.

        entity_type (Type[BaseEntityT]):
        The entity type class for which to retrieve the repository.

        Returns AbstractRepository[BaseEntityT]:
        The registered repository instance for the given entity type.
        """
        return self.repositories[entity_type]
