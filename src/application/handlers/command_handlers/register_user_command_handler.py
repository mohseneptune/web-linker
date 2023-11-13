import bcrypt

from domain.entities.user_entity import UserEntity
from domain.messages.commands.register_user_command import RegisterUserCommand
from domain.messages.events.user_created_event import UserCreatedEvent
from domain.unit_of_work import AbstractUnitOfWork


def register_user_command_handler(
    command: RegisterUserCommand, uow: AbstractUnitOfWork
):
    with uow:
        hashed_password = bcrypt.hashpw(
            command.password.encode("utf-8"), bcrypt.gensalt()
        )
        user = UserEntity.create(
            username=command.username,
            hashed_password=str(hashed_password),
            first_name=command.first_name,
            last_name=command.last_name,
        )
        user_repository = uow.get_repository(UserEntity)
        user.add_event(UserCreatedEvent(user_uuid=user.uuid))
        user_repository.add(user)

        uow.get_repository(UserEntity).add(user)
        uow.commit()
