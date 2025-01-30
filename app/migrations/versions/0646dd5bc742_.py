"""empty message

Revision ID: 0646dd5bc742
Revises: 672996a942dc
Create Date: 2025-01-25 18:13:19.311641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0646dd5bc742'
down_revision: Union[str, None] = '672996a942dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
