from typing import Optional

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from application.handlers.command_handlers.register_user_command_handler import (
    handle_register_user,
)
from application.message_bus import MessageBus
from domain.messages.commands.register_user_command import RegisterUserCommand
from infrastructure.sauow import SQLAlchemyUnitOfWork

bus = MessageBus(
    uow=SQLAlchemyUnitOfWork(),
    event_handlers={},
    command_handlers={RegisterUserCommand: handle_register_user},
)

router = APIRouter(prefix="/users", tags=["users"])


class RegisterUserRequestModel(BaseModel):
    username: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


@router.post("/register")
def register_user(user: RegisterUserRequestModel):
    command = RegisterUserCommand(**user.model_dump())
    bus.handle(command)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content={"message": "User created"}
    )
