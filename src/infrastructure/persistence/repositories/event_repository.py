from domain.entities.event_entity import EventEntity
from infrastructure.persistence.repositories.abstract_repository import (
    AbstractSQLAlchemyRepository,
)


class EventRepository(AbstractSQLAlchemyRepository[EventEntity]):
    @property
    def _entity_class(self):
        return EventEntity
