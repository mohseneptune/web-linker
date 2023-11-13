import json


class Message:
    pass


class BaseCommand(Message):
    pass


class BaseEvent(Message):
    """Base Event"""

    def to_dict(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
