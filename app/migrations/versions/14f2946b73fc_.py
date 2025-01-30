"""empty message

Revision ID: 14f2946b73fc
Revises: 24dc79d75000
Create Date: 2025-01-25 18:04:23.180006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14f2946b73fc'
down_revision: Union[str, None] = '24dc79d75000'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
