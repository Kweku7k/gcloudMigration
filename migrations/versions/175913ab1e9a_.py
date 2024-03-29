"""empty message

Revision ID: 175913ab1e9a
Revises: d6c0275f41b1
Create Date: 2022-11-27 16:33:31.811793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '175913ab1e9a'
down_revision = 'd6c0275f41b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket_transaction', sa.Column('code', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket_transaction', 'code')
    # ### end Alembic commands ###
