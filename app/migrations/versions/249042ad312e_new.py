"""new

Revision ID: 249042ad312e
Revises: ace0f50e5e0a
Create Date: 2025-01-26 10:17:40.775876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '249042ad312e'
down_revision: Union[str, None] = 'ace0f50e5e0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
