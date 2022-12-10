"""add content column to posts table

Revision ID: 94c3dce3009c
Revises: 76550c4060c2
Create Date: 2022-12-09 17:01:13.724076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c3dce3009c'
down_revision = '76550c4060c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
