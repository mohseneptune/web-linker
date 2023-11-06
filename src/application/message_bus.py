from typing import Callable, Dict, List, Type

from domain.messages.base_messages import BaseCommand, BaseEvent, Message
from domain.unit_of_work import AbstractUnitOfWork

EventHandler = Dict[Type[BaseEvent], List[Callable]]
CommandHandler = Dict[Type[BaseCommand], Callable]


class MessageBus:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
        event_handlers: EventHandler,
        command_handlers: CommandHandler,
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message) -> None:
        """Handle a message by calling the appropriate handler method."""
        if isinstance(message, BaseCommand):
            self._handle_command(message)
        elif isinstance(message, BaseEvent):
            self._handle_event(message)
        else:
            raise ValueError(f"Unknown message type: {type(message)}")

    def _handle_command(self, command: BaseCommand) -> None:
        # Get the handler based on the type of the command
        handler = self.command_handlers.get(type(command))
        # Check if the handler exists
        if handler is None:
            raise ValueError(f"No command handler registered for {type(command)}")
        # Call the handler with the command and the UoW
        handler(command, self.uow)

    def _handle_event(self, event: BaseEvent) -> None:
        handlers = self.event_handlers.get(type(event), [])
        for handler in handlers:
            handler(event, self.uow)
