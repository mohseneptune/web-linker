from typing import Generic, List, Optional, TypeVar
from uuid import UUID, uuid4

from domain.messages.base_messages import BaseEvent

E = TypeVar("E", bound=BaseEvent)


class BaseEntity(Generic[E]):
    """
    A base class for entities in a domain-driven design.

    This class is generic, allowing for type-safe association
    with events of a particular base type.
    Using generics, each entity subclass can specify the types of events
    it can produce, leading to a design
    where it is clear which entity is associated with
    which events and also enabling the use of various
    event types across different entities.

    id (Optional[int]): The primary key from the database;
        may be None if the entity has not been persisted.
    uuid (UUID): A universally unique identifier for the entity instance;
        useful for referencing the entity before it has a database ID.
    _events (List[E]): A list of domain events that are yet to be dispatched.
        These are typically cleared after the events are published.
    """

    def __init__(self):  # pylint: disable=redefined-builtin
        self.id: Optional[int] = None
        self.uuid: UUID = uuid4()
        self._events: List[E] = []

    def add_event(self, event: E) -> None:
        """Add a domain event to the entity's list of events."""
        self._events.append(event)

    def clear_events(self) -> None:
        """Clear all pending domain events."""
        self._events.clear()

    def get_events(self) -> List[E]:
        """
        Get a list of domain events.

        We return a copy of the events list to prevent outside modifications
        to the aggregate's internal state. This is a safeguard to maintain
        the integrity of the aggregate's domain events.
        """
        return list(self._events)

    def __eq__(self, other):
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id == other.id and self.id is not None

    def __hash__(self):
        return hash(self.id)
