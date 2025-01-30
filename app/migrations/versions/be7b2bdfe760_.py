"""empty message

Revision ID: be7b2bdfe760
Revises: 43c678e86fc2
Create Date: 2025-01-26 10:11:54.224973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be7b2bdfe760'
down_revision: Union[str, None] = '43c678e86fc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
