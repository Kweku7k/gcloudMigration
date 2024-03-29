"""empty message

Revision ID: 9e75cf767ac9
Revises: 4af233a6bf7b
Create Date: 2022-11-25 09:43:56.019793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e75cf767ac9'
down_revision = '4af233a6bf7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'typeOfTicket')
    op.add_column('ticket', sa.Column('typeOfTickets', sa.String(), nullable=True))
    op.drop_column('ticket', 'typeOfTicket')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('typeOfTicket', sa.VARCHAR(), nullable=True))
    op.add_column('customer', sa.Column('typeOfTicket', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
