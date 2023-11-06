from __future__ import annotations

from sqlalchemy.orm import Session, sessionmaker

from domain.unit_of_work import AbstractUnitOfWork
from infrastructure.database import POSTGRES_SESSION_FACTORY


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    session: Session

    def __init__(
        self, session_factory: sessionmaker = POSTGRES_SESSION_FACTORY
    ) -> None:
        self.session_factory = session_factory

    def __enter__(self) -> SQLAlchemyUnitOfWork:
        self.session = self.session_factory()
        # Here you would initialize your specific repositories if needed,
        # and register them with the unit of work.
        # Example:
        # self.register_repository(
        # SomeEntity, SQLAlchmeyRepositoryForSomeEntity(self.session)
        # )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self.session.close()

    def _commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
