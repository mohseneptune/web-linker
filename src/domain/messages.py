from dataclasses import dataclass


@dataclass
class Message:
    pass


@dataclass
class Command(Message):
    pass


@dataclass
class Event(Message):
    pass
