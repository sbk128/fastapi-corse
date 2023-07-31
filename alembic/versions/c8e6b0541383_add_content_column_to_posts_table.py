"""add content column to posts table

Revision ID: c8e6b0541383
Revises: d7e58251d584
Create Date: 2023-07-31 10:42:18.330977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e6b0541383'
down_revision = 'd7e58251d584'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
