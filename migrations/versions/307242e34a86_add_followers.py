"""add followers

Revision ID: 307242e34a86
Revises: cb0911b491f1
Create Date: 2018-06-27 23:04:51.450108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '307242e34a86'
down_revision = 'cb0911b491f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
