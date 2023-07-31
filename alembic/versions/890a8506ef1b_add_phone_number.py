"""add phone number

Revision ID: 890a8506ef1b
Revises: 6656abf1bc4c
Create Date: 2023-07-31 11:51:12.740489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '890a8506ef1b'
down_revision = '6656abf1bc4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    pass
    # ### end Alembic commands ###
