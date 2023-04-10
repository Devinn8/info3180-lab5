"""empty message

Revision ID: 36e5ce2e2ea0
Revises: 
Create Date: 2023-04-10 02:05:29.430303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36e5ce2e2ea0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('poster', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
