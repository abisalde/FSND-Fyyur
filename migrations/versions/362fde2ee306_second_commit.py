"""second-commit

Revision ID: 362fde2ee306
Revises: e52d8d1dcec4
Create Date: 2022-06-06 14:59:57.861003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '362fde2ee306'
down_revision = 'e52d8d1dcec4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('Artist', 'website')
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'website_link')
    op.add_column('Artist', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
