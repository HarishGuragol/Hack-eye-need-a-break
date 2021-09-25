from sqlalchemy import Integer, Column, Table, Float, ForeignKey, String

from db.meta import metadata

Score = Table("score", metadata,
    Column("id", Integer(), primary_key=True),
    Column("user_id", Integer(), ForeignKey("user.id"), nullable=False),
    Column("score", Float(), primary_key=True),
    Column("timestamp", Float(), primary_key=True)
)