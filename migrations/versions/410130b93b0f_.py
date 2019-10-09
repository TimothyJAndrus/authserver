"""empty message

Revision ID: 410130b93b0f
Revises: 6eee1715ff21
Create Date: 2019-10-09 00:29:03.197730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '410130b93b0f'
down_revision = '6eee1715ff21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oauth2_authorization_codes', sa.Column('code_challenge', sa.VARCHAR(), nullable=True))
    op.add_column('oauth2_authorization_codes', sa.Column('code_challenge_method', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('oauth2_authorization_codes', 'code_challenge_method')
    op.drop_column('oauth2_authorization_codes', 'code_challenge')
    # ### end Alembic commands ###