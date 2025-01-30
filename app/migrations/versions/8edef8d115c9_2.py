"""2

Revision ID: 8edef8d115c9
Revises: 249042ad312e
Create Date: 2025-01-26 10:20:16.392681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8edef8d115c9'
down_revision: Union[str, None] = '249042ad312e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
