from application.dependency_injector import inject_dependencies
from application.handlers.hanlders_collector import (
    collect_command_handlers,
    collect_event_handlers,
)
from application.message_bus import MessageBus
from infrastructure.redis_event_publisher import RedisEventPublisher
from infrastructure.sauow import SQLAlchemyUnitOfWork


def bootstrap() -> MessageBus:
    uow = SQLAlchemyUnitOfWork()
    event_publisher = RedisEventPublisher()

    dependencies = {"uow": uow, "publish": event_publisher.publish}

    command_handlers = collect_command_handlers()
    event_handlers = collect_event_handlers()

    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in command_handlers.items()
    }

    injected_event_handlers = {
        event_type: [inject_dependencies(handler, dependencies) for handler in handlers]
        for event_type, handlers in event_handlers.items()
    }

    return MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )
