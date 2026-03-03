"""split full_name

Revision ID: 307456355dea
Revises: 4550e751363e
Create Date: 2026-03-02 22:49:32.710152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '307456355dea'
down_revision: Union[str, Sequence[str], None] = '4550e751363e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()

    # Check and add 'first_name'
    result = conn.execute(
        sa.text(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name='users' AND column_name='first_name';"
        )
    )
    if not result.fetchone():
        op.add_column("users", sa.Column("first_name", sa.String()))

    # Check and add 'last_name'
    result = conn.execute(
        sa.text(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name='users' AND column_name='last_name';"
        )
    )
    if not result.fetchone():
        op.add_column("users", sa.Column("last_name", sa.String()))

    results = conn.execute(sa.text("SELECT id, full_name FROM users"))
    for row in results:
        parts = row.full_name.split(" ")
        first = parts[0]
        last = parts[-1] if len(parts) > 1 else ""
        conn.execute(
            sa.text(
                "UPDATE users SET first_name=:f, last_name=:l WHERE id=:i"
            ),
            {"f": first, "l": last, "i": row.id}
        )

# ...existing code...

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "first_name")
    op.drop_column("users", "last_name")
