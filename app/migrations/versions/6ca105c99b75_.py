"""empty message

Revision ID: 6ca105c99b75
Revises: 14f2946b73fc
Create Date: 2025-01-25 18:05:43.775085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ca105c99b75'
down_revision: Union[str, None] = '14f2946b73fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
