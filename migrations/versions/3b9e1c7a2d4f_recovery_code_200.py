"""recovery_code com 200 caracteres

Revision ID: 3b9e1c7a2d4f
Revises: ffd0b6965d26
Create Date: 2026-10-12 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b9e1c7a2d4f'
down_revision = 'ffd0b6965d26'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('recovery_code',
               existing_type=sa.String(length=100),
               type_=sa.String(length=200),
               existing_nullable=True)


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('recovery_code',
               existing_type=sa.String(length=200),
               type_=sa.String(length=100),
               existing_nullable=True)
