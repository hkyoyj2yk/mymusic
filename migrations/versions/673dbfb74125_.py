"""empty message

Revision ID: 673dbfb74125
Revises: e3bdd4551fa0
Create Date: 2022-01-08 08:19:17.110974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '673dbfb74125'
down_revision = 'e3bdd4551fa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('music_rec', sa.Column('singer', sa.Text(), nullable=True))
    op.add_column('music_rec', sa.Column('lyrics', sa.Text(), nullable=True))
    op.add_column('music_rec', sa.Column('genre', sa.Text(), nullable=True))
    op.add_column('music_rec', sa.Column('grade', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('music_rec', 'grade')
    op.drop_column('music_rec', 'genre')
    op.drop_column('music_rec', 'lyrics')
    op.drop_column('music_rec', 'singer')
    # ### end Alembic commands ###
