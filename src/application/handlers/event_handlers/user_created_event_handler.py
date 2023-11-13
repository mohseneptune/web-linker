import logging

from src.domain.messages.events.user_created_event import UserCreatedEvent


def user_created_event_handler(event: UserCreatedEvent):
    logging.info("User created: %s", event.user_uuid)
