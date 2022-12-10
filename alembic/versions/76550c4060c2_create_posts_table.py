"""Create posts table

Revision ID: 76550c4060c2
Revises: 
Create Date: 2022-12-09 16:15:37.083840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76550c4060c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
