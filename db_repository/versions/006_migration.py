from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('rid', INTEGER, primary_key=True, nullable=False),
    Column('sender', INTEGER),
    Column('receiver', INTEGER),
    Column('confirmed', BOOLEAN),
)

post = Table('post', pre_meta,
    Column('pid', INTEGER, primary_key=True, nullable=False),
    Column('content', VARCHAR(length=140)),
    Column('posted', DATETIME),
    Column('writer', INTEGER),
    Column('pic', VARCHAR(length=1000)),
    Column('wid', INTEGER),
    Column('belongs', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    pre_meta.tables['post'].columns['belongs'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    pre_meta.tables['post'].columns['belongs'].create()
