from __future__ import annotations

from typing import Optional

from domain.entities.base_entity import BaseEntity
from domain.messages.events.user_created_event import UserCreatedEvent


class UserEntity(BaseEntity):
    def __init__(
        self,
        username: str,
        hashed_password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ):
        super().__init__()
        self.username = username
        self.hashed_password = hashed_password
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def create(cls, username: str, hashed_password: str, **kwargs) -> UserEntity:
        """
        Factory method to create a new UserEntity instance and publish
        a UserCreatedEvent domain event.
        """
        user = cls(username, hashed_password, **kwargs)
        user.add_event(UserCreatedEvent(user_uuid=user.uuid))
        return user
