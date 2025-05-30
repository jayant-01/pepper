"""add template_data to FormTemplate model

Revision ID: 97091fb594ac
Revises: dc0986e2e96f
Create Date: 2025-04-29 13:09:54.432490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97091fb594ac'
down_revision = 'dc0986e2e96f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form_template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('template_data', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form_template', schema=None) as batch_op:
        batch_op.drop_column('template_data')

    # ### end Alembic commands ###
