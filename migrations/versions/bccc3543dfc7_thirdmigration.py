"""ThirdMigration

Revision ID: bccc3543dfc7
Revises: 5e10fd322bd0
Create Date: 2023-02-22 16:41:22.676606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bccc3543dfc7'
down_revision = '5e10fd322bd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('account')

    # ### end Alembic commands ###
