"""add index to mobile_number

Revision ID: 4550e751363e
Revises: e796b6067c33
Create Date: 2026-03-02 22:48:03.716133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4550e751363e'
down_revision: Union[str, Sequence[str], None] = 'e796b6067c33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index("ix_users_mobile_number", "users", ["mobile_number"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ix_users_mobile_number", table_name="users")
