"""create_animal_table

Revision ID: fbb388ce7c75
Revises: c9730e08ea19
Create Date: 2018-12-02 17:20:09.987287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbb388ce7c75'
down_revision = 'c6d3d310fea5'
branch_labels = None
depends_on = None


table_name = 'animal'


def upgrade():
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('animal_type_id', sa.Integer, sa.ForeignKey('animal_type.id')),
        sa.Column('name', sa.String(50)),
        sa.Column('weight', sa.Numeric),
        sa.Column('age', sa.Integer),
    )


def downgrade():
    op.drop_table(table_name)
