"""empty message

Revision ID: 0c626aebd216
Revises: 84be851b532c
Create Date: 2022-11-25 08:07:30.431647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c626aebd216'
down_revision = '84be851b532c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('event', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'event')
    # ### end Alembic commands ###