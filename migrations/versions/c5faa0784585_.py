"""empty message

Revision ID: c5faa0784585
Revises: a367f4c31fc7
Create Date: 2022-11-25 09:27:17.198109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5faa0784585'
down_revision = 'a367f4c31fc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('typeOfTicket', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'typeOfTicket')
    # ### end Alembic commands ###
