"""add last few columns to posts table

Revision ID: adfcbdb7a7c4
Revises: 8b6f25da70b4
Create Date: 2022-12-09 20:05:54.352792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adfcbdb7a7c4'
down_revision = '8b6f25da70b4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
