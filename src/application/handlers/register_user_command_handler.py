# src/application/handlers/user_command_handlers.py

import bcrypt

from domain.entities.user_entity import UserEntity
from domain.messages.commands.register_user_command import RegisterUserCommand
from domain.unit_of_work import AbstractUnitOfWork


def handle_register_user(command: RegisterUserCommand, uow: AbstractUnitOfWork):
    with uow:
        # You would typically hash the password before saving.
        hashed_password = bcrypt.hashpw(
            command.password.encode("utf-8"), bcrypt.gensalt()
        )

        # Use a factory method or constructor to create the UserEntity
        user = UserEntity.create(
            username=command.username,
            hashed_password=str(hashed_password),
            first_name=command.first_name,
            last_name=command.last_name,
        )

        # Add the new user entity to the repository
        uow.get_repository(UserEntity).add(user)

        # Commit the unit of work
        uow.commit()
