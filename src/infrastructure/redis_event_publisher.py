import json

from redis import Redis  # type: ignore

from domain.messages.base_messages import BaseEvent
from domain.messages.event_publisher import AbstractEventPublisher
from settings import REDIS_DATABASE_URI


class RedisEventPublisher(AbstractEventPublisher):
    def __init__(self, client: Redis = Redis.from_url(REDIS_DATABASE_URI)):
        self.client = client

    def publish(self, channel: str, event: BaseEvent) -> None:
        self.client.publish(channel, json.dumps(event))

    def get_client(self) -> Redis:
        return self.client
