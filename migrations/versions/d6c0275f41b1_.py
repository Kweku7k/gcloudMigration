"""empty message

Revision ID: d6c0275f41b1
Revises: b3bc173cd9f4
Create Date: 2022-11-27 16:19:00.127930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6c0275f41b1'
down_revision = 'b3bc173cd9f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('cost', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'cost')
    # ### end Alembic commands ###