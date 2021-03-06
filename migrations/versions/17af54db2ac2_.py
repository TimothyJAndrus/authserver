"""empty message

Revision ID: 17af54db2ac2
Revises: 7998aa29b531
Create Date: 2019-07-26 02:17:24.396487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17af54db2ac2'
down_revision = '7998aa29b531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('oauth2_client',
    sa.Column('client_id', sa.String(length=48), nullable=True),
    sa.Column('client_secret', sa.String(length=120), nullable=True),
    sa.Column('issued_at', sa.Integer(), nullable=False),
    sa.Column('expires_at', sa.Integer(), nullable=False),
    sa.Column('redirect_uri', sa.Text(), nullable=True),
    sa.Column('token_endpoint_auth_method', sa.String(length=48), nullable=True),
    sa.Column('grant_type', sa.Text(), nullable=False),
    sa.Column('response_type', sa.Text(), nullable=False),
    sa.Column('scope', sa.Text(), nullable=False),
    sa.Column('client_name', sa.String(length=100), nullable=True),
    sa.Column('client_uri', sa.Text(), nullable=True),
    sa.Column('logo_uri', sa.Text(), nullable=True),
    sa.Column('contact', sa.Text(), nullable=True),
    sa.Column('tos_uri', sa.Text(), nullable=True),
    sa.Column('policy_uri', sa.Text(), nullable=True),
    sa.Column('jwks_uri', sa.Text(), nullable=True),
    sa.Column('jwks_text', sa.Text(), nullable=True),
    sa.Column('i18n_metadata', sa.Text(), nullable=True),
    sa.Column('software_id', sa.String(length=36), nullable=True),
    sa.Column('software_version', sa.String(length=48), nullable=True),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_oauth2_client_client_id'), 'oauth2_client', ['client_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_oauth2_client_client_id'), table_name='oauth2_client')
    op.drop_table('oauth2_client')
    # ### end Alembic commands ###
