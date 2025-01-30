"""authors

Revision ID: ace0f50e5e0a
Revises: a56f97453da6
Create Date: 2025-01-26 10:13:51.076237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ace0f50e5e0a'
down_revision: Union[str, None] = 'a56f97453da6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
