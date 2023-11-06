from uuid import UUID

from domain.messages.base_messages import BaseEvent


class UserCreatedEvent(BaseEvent):
    def __init__(self, user_uuid: UUID):
        self.user_uuid = user_uuid
