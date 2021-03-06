from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
connection = Table('connection', pre_meta,
    Column('cid', INTEGER, primary_key=True, nullable=False),
    Column('sender', INTEGER),
    Column('receiver', INTEGER),
)

request = Table('request', post_meta,
    Column('rid', Integer, primary_key=True, nullable=False),
    Column('sender', Integer),
    Column('receiver', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['connection'].drop()
    post_meta.tables['request'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['connection'].create()
    post_meta.tables['request'].drop()
