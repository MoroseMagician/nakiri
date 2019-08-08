"""Change password column type

Revision ID: 1e87378817de
Revises: 5802d2878b99
Create Date: 2019-08-08 02:26:59.429260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e87378817de'
down_revision = '5802d2878b99'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        table_name='user',
        column_name='password',
        type_=sa.Text
    )


def downgrade():
    op.alter_column(
        table_name='user',
        column_name='password',
        type_=sa.String(128)
    )
