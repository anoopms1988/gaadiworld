"""create account table

Revision ID: 2f0c8274d09a
Revises: 103654a199c4
Create Date: 2017-06-01 14:47:12.334321

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2f0c8274d09a'
down_revision = '103654a199c4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'account',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50), nullable=False),
            sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
