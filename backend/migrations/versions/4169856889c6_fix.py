"""fix

Revision ID: 4169856889c6
Revises: 4fb6d0fe85d9
Create Date: 2023-12-21 04:56:38.412187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '4169856889c6'
down_revision: Union[str, None] = '4fb6d0fe85d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('genre_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('budget', sa.Integer(), nullable=False),
    sa.Column('homepage', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('overview', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('popularity', sa.Float(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('revenue', sa.Integer(), nullable=False),
    sa.Column('runtime', sa.Integer(), nullable=False),
    sa.Column('movie_status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tagline', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('vote_average', sa.Float(), nullable=False),
    sa.Column('vote_count', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moviegenrelink',
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('genre_id', 'movie_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moviegenrelink')
    op.drop_table('movies')
    op.drop_table('genres')
    # ### end Alembic commands ###