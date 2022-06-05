"""empty message

Revision ID: b05f1f9a76cd
Revises: 9245249e6446
Create Date: 2022-06-04 13:45:51.086567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b05f1f9a76cd'
down_revision = '9245249e6446'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('artist', sa.Column('seeking_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'seeking_description')
    op.drop_column('artist', 'seeking_venue')
    op.drop_column('artist', 'website_link')
    # ### end Alembic commands ###
