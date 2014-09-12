__author__ = 'buyvich'

import sqlalchemy as sa

meta = sa.MetaData()

training = sa.Table('t_training', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(50)),
    sa.Column('goal', sa.Integer),
    sa.Column('tng_type', sa.String(15)),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('t_user.id'))
)

user = sa.Table('t_user', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('login', sa.String(128)),
    sa.Column('password', sa.String(256)),
)
