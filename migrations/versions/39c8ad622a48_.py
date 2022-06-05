"""empty message

Revision ID: 39c8ad622a48
Revises: 6ed8df207444
Create Date: 2022-06-04 17:39:48.292435

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '39c8ad622a48'
down_revision = '6ed8df207444'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('show', 'id')
    # ### end Alembic commands ###
