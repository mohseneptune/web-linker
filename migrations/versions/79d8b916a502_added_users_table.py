# pylint: disable=E1101,W0401,W0614,C0103
"""Added users table

Revision ID: 79d8b916a502
Revises: 
Create Date: 2023-11-06 17:24:28.369314

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "79d8b916a502"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create account schema, i create this code manually
    op.execute("CREATE SCHEMA IF NOT EXISTS accounts")

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("first_name", sa.String(length=50), nullable=True),
        sa.Column("last_name", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
        schema="accounts",
    )
    op.create_index(
        op.f("ix_accounts_users_id"), "users", ["id"], unique=False, schema="accounts"
    )
    op.create_index(
        op.f("ix_accounts_users_uuid"),
        "users",
        ["uuid"],
        unique=True,
        schema="accounts",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_accounts_users_uuid"), table_name="users", schema="accounts")
    op.drop_index(op.f("ix_accounts_users_id"), table_name="users", schema="accounts")
    op.drop_table("users", schema="accounts")
    # ### end Alembic commands ###

    # Drop account schema, i create this code manually
    op.execute("DROP SCHEMA IF EXISTS accounts")