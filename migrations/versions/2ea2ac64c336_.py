"""empty message

Revision ID: 2ea2ac64c336
Revises: 
Create Date: 2020-02-01 17:03:17.155187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ea2ac64c336'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Grade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Semester',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['grade_id'], ['Grade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Module',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('semester_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['grade_id'], ['Grade.id'], ),
    sa.ForeignKeyConstraint(['semester_id'], ['Semester.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('MCQs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('choice_A', sa.String(), nullable=False),
    sa.Column('choice_B', sa.String(), nullable=False),
    sa.Column('choice_C', sa.String(), nullable=False),
    sa.Column('choice_D', sa.String(), nullable=False),
    sa.Column('choice_E', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('module_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['module_id'], ['Module.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('MCQs')
    op.drop_table('Module')
    op.drop_table('Semester')
    op.drop_table('Grade')
    # ### end Alembic commands ###
