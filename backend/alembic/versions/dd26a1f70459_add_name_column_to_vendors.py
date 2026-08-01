"""add name column to vendors

Revision ID: dd26a1f70459
Revises: 0169dd7b7b8a
Create Date: 2026-07-28 16:38:40.894654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd26a1f70459'
down_revision: Union[str, Sequence[str], None] = '0169dd7b7b8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "vendors",
        sa.Column("name", sa.String(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column(
        "vendors",
        "name"
    )
