import bcrypt

from domain.entities.user_entity import UserEntity
from domain.messages.commands.register_user_command import RegisterUserCommand
from domain.unit_of_work import AbstractUnitOfWork


def handle_register_user(command: RegisterUserCommand, uow: AbstractUnitOfWork):
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
        uow.get_repository(UserEntity).add(user)
        uow.commit()
