"""empty message

Revision ID: b3d42c882a3e
Revises: 3275038473b7
Create Date: 2020-11-20 13:39:47.550768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3d42c882a3e'
down_revision = '3275038473b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'category', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='unique')
    # ### end Alembic commands ###
