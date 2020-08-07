"""tables

Revision ID: 254ee7ca6775
Revises: 
Create Date: 2020-08-02 00:41:19.082109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254ee7ca6775'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('department', sa.String(length=64), nullable=True),
    sa.Column('usertype', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_email'), 'admin', ['email'], unique=True)
    op.create_index(op.f('ix_admin_username'), 'admin', ['username'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('fname', sa.String(length=64), nullable=True),
    sa.Column('lname', sa.String(length=64), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('zip', sa.String(length=5), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_fname'), 'user', ['fname'], unique=False)
    op.create_index(op.f('ix_user_lname'), 'user', ['lname'], unique=False)
    op.create_index(op.f('ix_user_phone'), 'user', ['phone'], unique=True)
    op.create_index(op.f('ix_user_score'), 'user', ['score'], unique=False)
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_index(op.f('ix_user_score'), table_name='user')
    op.drop_index(op.f('ix_user_phone'), table_name='user')
    op.drop_index(op.f('ix_user_lname'), table_name='user')
    op.drop_index(op.f('ix_user_fname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_admin_username'), table_name='admin')
    op.drop_index(op.f('ix_admin_email'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###