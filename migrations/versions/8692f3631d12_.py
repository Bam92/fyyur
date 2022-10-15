"""empty message

Revision ID: 8692f3631d12
Revises: d050ffc70bb9
Create Date: 2022-10-14 15:54:56.580809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8692f3631d12'
down_revision = 'd050ffc70bb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    # ### end Alembic commands ###
