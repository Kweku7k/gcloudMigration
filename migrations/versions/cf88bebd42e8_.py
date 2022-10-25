"""empty message

Revision ID: cf88bebd42e8
Revises: e7dbec88afd9
Create Date: 2022-10-25 14:31:59.306808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf88bebd42e8'
down_revision = 'e7dbec88afd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sessionId', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phoneNumber', sa.String(), nullable=True),
    sa.Column('numberOfTickets', sa.String(), nullable=True),
    sa.Column('typeOfTickets', sa.String(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('paymentId', sa.String(), nullable=True),
    sa.Column('startDate', sa.String(), nullable=True),
    sa.Column('event', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###
