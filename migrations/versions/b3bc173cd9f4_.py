"""empty message

Revision ID: b3bc173cd9f4
Revises: cd03cbfbe865
Create Date: 2022-11-27 15:54:01.037417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3bc173cd9f4'
down_revision = 'cd03cbfbe865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('code', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'code')
    # ### end Alembic commands ###
