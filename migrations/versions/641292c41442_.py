"""empty message

Revision ID: 641292c41442
Revises: 17af54db2ac2
Create Date: 2019-07-26 07:39:59.923436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '641292c41442'
down_revision = '17af54db2ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.add_column('users', sa.Column('salt', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'salt')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###