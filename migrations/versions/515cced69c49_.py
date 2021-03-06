"""empty message

Revision ID: 515cced69c49
Revises: 
Create Date: 2020-06-27 17:17:56.027880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '515cced69c49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kill_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_kills', sa.VARCHAR(length=6), nullable=True),
    sa.Column('time_stamp', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kill_history')
    # ### end Alembic commands ###
