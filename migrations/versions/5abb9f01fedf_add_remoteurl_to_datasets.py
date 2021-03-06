"""Add remoteUrl to datasets

Revision ID: 5abb9f01fedf
Revises: ab927684d5ea
Create Date: 2021-02-18 14:26:34.551345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5abb9f01fedf'
down_revision = 'ab927684d5ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('datasets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('remoteUrl', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('datasets', schema=None) as batch_op:
        batch_op.drop_column('remoteUrl')

    # ### end Alembic commands ###
