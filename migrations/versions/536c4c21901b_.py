"""empty message

Revision ID: 536c4c21901b
Revises: 4035a33db219
Create Date: 2022-01-08 10:48:12.910662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536c4c21901b'
down_revision = '4035a33db219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diary', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_diary_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diary', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_diary_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###