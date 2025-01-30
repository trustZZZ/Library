"""empty message

Revision ID: 43c678e86fc2
Revises: 0646dd5bc742
Create Date: 2025-01-26 10:08:04.804825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43c678e86fc2'
down_revision: Union[str, None] = '0646dd5bc742'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
