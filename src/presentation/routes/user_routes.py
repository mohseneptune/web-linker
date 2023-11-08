# src/presentation/routers/user_router.py

from typing import Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from application.handlers.register_user_command_handler import handle_register_user
from application.message_bus import MessageBus
from domain.messages.commands.register_user_command import RegisterUserCommand
from infrastructure.sauow import SQLAlchemyUnitOfWork

uow = SQLAlchemyUnitOfWork()

bus = MessageBus(
    uow=uow,
    event_handlers={},
    command_handlers={RegisterUserCommand: handle_register_user},
)

router = APIRouter(prefix="/users", tags=["users"])


class RegisterUserRequestModel(BaseModel):
    username: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: RegisterUserRequestModel):
    # Instantiate the command with the request data
    command = RegisterUserCommand(
        username=user.username,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    try:
        # Handle the command
        bus.handle(command)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e

    return {"status": "success", "message": "User registered successfully."}
