"""empty message

Revision ID: cc0a2aa182
Revises: 00000000
Create Date: 2020-05-23 05:11:16.946267

"""

# revision identifiers, used by Alembic.
revision = 'cc0a2aa182'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute(''' 
        UPDATE user SET point_balance=5000 where user_id = 1
    ''')

    op.execute('''
        INSERT INTO rel_user (user_id, rel_lookup, attribute) VALUES (2, 'LOCATION', 'USA')
    ''')

    op.execute(''' 
        UPDATE user SET tier="Silver" where user_id = 3
    ''')


def downgrade():
    pass
