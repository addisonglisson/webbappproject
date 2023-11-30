"""Initial Study Pod Attempt migrations

Revision ID: 7f10d82191ea
Revises: 5f3d020f1d1c
Create Date: 2023-09-05 20:43:21.007532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f10d82191ea'
down_revision = '5f3d020f1d1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('study_pod',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('study_pod_members',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('study_pod_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['study_pod_id'], ['study_pod.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'study_pod_id')
    )
    op.create_table('study_pod_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('study_pod_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['study_pod_id'], ['study_pod.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('study_pod_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('study_pod_post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['study_pod_post_id'], ['study_pod_post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('study_pod_comment')
    op.drop_table('study_pod_post')
    op.drop_table('study_pod_members')
    op.drop_table('study_pod')
    # ### end Alembic commands ###