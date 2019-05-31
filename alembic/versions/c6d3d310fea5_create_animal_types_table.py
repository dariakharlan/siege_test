"""create_animal_types_table

Revision ID: c6d3d310fea5
Revises: 
Create Date: 2018-12-02 13:19:22.906736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6d3d310fea5'
down_revision = None
branch_labels = None
depends_on = None


table_name = 'animal_type'


def upgrade():
    table = op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), unique=True),
        sa.Column('deposit_cost', sa.Numeric),
        sa.Column('min_food_cost', sa.Numeric),
        sa.Column('max_food_cost', sa.Numeric),
    )
    op.bulk_insert(table, [
        {'id': 1, 'name': 'Dog', 'deposit_cost': 20, 'min_food_cost': 5, 'max_food_cost': 10},
        {'id': 2, 'name': 'Cat', 'deposit_cost': 15, 'min_food_cost': 2, 'max_food_cost': 8},
        {'id': 3, 'name': 'Turtle', 'deposit_cost': 10, 'min_food_cost': 3, 'max_food_cost': 5},
        {'id': 4, 'name': 'Mouse', 'deposit_cost': 8, 'min_food_cost': 2, 'max_food_cost': 2},
    ])


def downgrade():
    op.drop_table(table_name)
