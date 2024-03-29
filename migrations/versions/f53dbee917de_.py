"""empty message

Revision ID: f53dbee917de
Revises: c5faa0784585
Create Date: 2022-11-25 09:36:57.564892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f53dbee917de'
down_revision = 'c5faa0784585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('typeOfTicket', sa.String(), nullable=True))
    op.drop_column('customer', 'typeOfTickets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('typeOfTickets', sa.VARCHAR(), nullable=True))
    op.drop_column('customer', 'typeOfTicket')
    # ### end Alembic commands ###
