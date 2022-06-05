"""empty message

Revision ID: fc1b53cfbb44
Revises: 0b27a64b92b2
Create Date: 2022-06-04 22:16:58.663516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc1b53cfbb44'
down_revision = '0b27a64b92b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'show', 'venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.drop_column('show', 'venue_id')
    # ### end Alembic commands ###
