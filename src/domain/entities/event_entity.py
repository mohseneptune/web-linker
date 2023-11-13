from __future__ import annotations

from domain.entities.base_entity import BaseEntity


class EventEntity(BaseEntity):
    def __init__(self, event_type: str, payload: dict, is_processed: bool = False):
        super().__init__()
        self.event_type = event_type
        self.payload = payload
        self.is_processed = is_processed

    @classmethod
    def create(cls, event_type: str, payload: dict) -> EventEntity:
        """
        Factory method to create a new EventEntity instance.
        """
        event = cls(event_type, payload)
        return event
