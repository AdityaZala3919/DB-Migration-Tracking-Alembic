"""rename phone_number to mobile_number

Revision ID: e796b6067c33
Revises: 98fe1d485507
Create Date: 2026-03-02 22:46:51.614210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e796b6067c33'
down_revision: Union[str, Sequence[str], None] = '98fe1d485507'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("users", "phone_number", new_column_name="mobile_number")


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("users", "mobile_number", new_column_name="phone_number")
