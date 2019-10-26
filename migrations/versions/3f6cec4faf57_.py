"""empty message

Revision ID: 3f6cec4faf57
Revises: 
Create Date: 2019-10-25 12:04:54.348279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6cec4faf57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lead', sa.Column('addr_city', sa.String(length=20), nullable=True))
    op.add_column('lead', sa.Column('addr_state', sa.String(length=20), nullable=True))
    op.add_column('lead', sa.Column('address_line', sa.String(length=40), nullable=True))
    op.add_column('lead', sa.Column('country', sa.String(length=20), nullable=True))
    op.add_column('lead', sa.Column('notes', sa.String(length=100), nullable=True))
    op.add_column('lead', sa.Column('post_code', sa.String(length=20), nullable=True))
    op.add_column('lead', sa.Column('title', sa.String(length=100), nullable=True))
    op.create_foreign_key(None, 'lead', 'user', ['owner_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lead', type_='foreignkey')
    op.drop_column('lead', 'title')
    op.drop_column('lead', 'post_code')
    op.drop_column('lead', 'notes')
    op.drop_column('lead', 'country')
    op.drop_column('lead', 'address_line')
    op.drop_column('lead', 'addr_state')
    op.drop_column('lead', 'addr_city')
    # ### end Alembic commands ###