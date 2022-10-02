"""project models

Revision ID: f368fadbf244
Revises: 61adf3ed7ffe
Create Date: 2022-09-30 14:47:55.230898

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f368fadbf244'
down_revision = '61adf3ed7ffe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('filename', sa.String(length=25), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_filename'), 'project', ['filename'], unique=True)
    op.create_index(op.f('ix_project_name'), 'project', ['name'], unique=True)
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('page_num', sa.Integer(), nullable=False),
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('text_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_id', sa.Integer(), nullable=True),
    sa.Column('text_line', sa.String(length=10000), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text_line_id', sa.Integer(), nullable=True),
    sa.Column('char', sa.String(length=1), nullable=False),
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('x0', sa.Float(), nullable=False),
    sa.Column('y0', sa.Float(), nullable=False),
    sa.Column('x1', sa.Float(), nullable=False),
    sa.Column('y1', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['text_line_id'], ['text_line.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('user', 'public_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('user', 'public_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_table('character')
    op.drop_table('text_line')
    op.drop_table('page')
    op.drop_table('customer')
    op.drop_index(op.f('ix_project_name'), table_name='project')
    op.drop_index(op.f('ix_project_filename'), table_name='project')
    op.drop_table('project')
    # ### end Alembic commands ###
