from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
lift_entry = Table('lift_entry', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('lift', String(length=128)),
    Column('bw', Float),
    Column('weight', Float),
    Column('reps', Integer),
    Column('rpe', Float),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['lift_entry'].columns['rpe'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['lift_entry'].columns['rpe'].drop()
