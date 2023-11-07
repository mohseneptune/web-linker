from __future__ import annotations

from typing import Type

from sqlalchemy.orm import Session, sessionmaker

from domain.entities.base_entity import BaseEntity
from domain.entities.user_entity import UserEntity
from domain.repository import AbstractRepository
from domain.unit_of_work import AbstractUnitOfWork
from infrastructure.persistence.database import POSTGRES_SESSION_FACTORY
from infrastructure.persistence.repositories.user_repository import UserRepository


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    session: Session

    def __init__(
        self, session_factory: sessionmaker = POSTGRES_SESSION_FACTORY
    ) -> None:
        self.session_factory = session_factory

    def __enter__(self) -> SQLAlchemyUnitOfWork:
        self.session = self.session_factory()

        self.repositories[UserEntity] = UserRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self.session.close()

    def _commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def get_repository(
        self, entity_type: Type[BaseEntity]
    ) -> AbstractRepository[BaseEntity]:
        repo = self.repositories.get(entity_type)
        if not repo:
            raise NotImplementedError(
                f"Repository for entity {entity_type} not implemented"
            )
        return repo
