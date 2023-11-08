from dataclasses import dataclass
from typing import Optional

from domain.messages.base_messages import BaseCommand


@dataclass
class RegisterUserCommand(BaseCommand):
    username: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
