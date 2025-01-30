"""empty message

Revision ID: a56f97453da6
Revises: be7b2bdfe760
Create Date: 2025-01-26 10:12:38.894929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a56f97453da6'
down_revision: Union[str, None] = 'be7b2bdfe760'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
