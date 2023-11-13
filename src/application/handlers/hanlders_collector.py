import importlib
import inspect

from application.message_bus import CommandHandler, EventHandler

COMMAND_HANDLERS_MODULE = "application.handlers.command_handlers"
EVENT_HANDLERS_MODULE = "application.handlers.event_handlers"


def collect_command_handlers(
    module_path: str = COMMAND_HANDLERS_MODULE,
) -> CommandHandler:
    command_handlers: CommandHandler = {}
    module = importlib.import_module(module_path)

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and name.endswith("_handler"):
            command_type = obj.__annotations__.get("command")
            if command_type:
                command_handlers[command_type] = obj

    return command_handlers


def collect_event_handlers(module_path: str = EVENT_HANDLERS_MODULE) -> EventHandler:
    event_handlers: EventHandler = {}
    module = importlib.import_module(module_path)

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and name.endswith("_handler"):
            event_type = obj.__annotations__.get("event")
            if event_type:
                if event_type not in event_handlers:
                    event_handlers[event_type] = []
                event_handlers[event_type].append(obj)

    return event_handlers
