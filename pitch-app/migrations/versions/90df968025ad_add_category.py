"""add category

Revision ID: 90df968025ad
Revises: 6a25a6e0aea0
Create Date: 2019-02-27 20:39:39.795164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90df968025ad'
down_revision = '6a25a6e0aea0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
