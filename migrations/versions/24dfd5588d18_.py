"""empty message

Revision ID: 24dfd5588d18
Revises: 6321087511df
Create Date: 2022-11-25 09:38:39.052312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24dfd5588d18'
down_revision = '6321087511df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'typeOfTicket')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('typeOfTicket', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
