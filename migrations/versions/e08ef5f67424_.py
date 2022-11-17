"""empty message

Revision ID: e08ef5f67424
Revises: 7998c55358e2
Create Date: 2022-11-17 01:40:52.336123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e08ef5f67424'
down_revision = '7998c55358e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poll', 'talanku')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poll', sa.Column('talanku', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###