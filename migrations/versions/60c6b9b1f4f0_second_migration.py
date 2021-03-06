"""Second migration.

Revision ID: 60c6b9b1f4f0
Revises: 0c71854d4009
Create Date: 2022-07-12 13:20:03.752277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c6b9b1f4f0'
down_revision = '0c71854d4009'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_name', sa.String(length=25), nullable=False),
    sa.Column('review_first_name', sa.String(length=25), nullable=False),
    sa.Column('review_last_name', sa.String(length=25), nullable=False),
    sa.Column('review_email', sa.String(length=25), nullable=False),
    sa.Column('review_date', sa.Date(), nullable=False),
    sa.Column('review_venue', sa.String(length=25), nullable=True),
    sa.Column('review_content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('review_email'),
    sa.UniqueConstraint('review_first_name'),
    sa.UniqueConstraint('review_last_name'),
    sa.UniqueConstraint('review_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###
