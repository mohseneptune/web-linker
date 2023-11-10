from abc import ABC, abstractmethod

from domain.messages.base_messages import BaseEvent


class AbstractEventPublisher(ABC):
    @abstractmethod
    def publish(self, channel: str, event: BaseEvent) -> None:
        """Publish an event to the specified channel."""
        raise NotImplementedError
