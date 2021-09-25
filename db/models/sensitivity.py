from sqlalchemy import Integer, Column, Table, Float, ForeignKey, String

from db.meta import metadata


Sensitivity = Table("sensitivity", metadata,
    Column("id", Integer(), primary_key=True),
    Column("user_id", Integer(), ForeignKey("user.id"), nullable=False),
    Column("value", Float(), primary_key=True),
)