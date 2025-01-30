"""empty message

Revision ID: 672996a942dc
Revises: 6ca105c99b75
Create Date: 2025-01-25 18:12:20.004266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '672996a942dc'
down_revision: Union[str, None] = '6ca105c99b75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
