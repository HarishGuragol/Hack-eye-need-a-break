from sqlalchemy import Integer, Column, Table, Float, ForeignKey, String

from db.meta import metadata

EyeData = Table("eye_data", metadata,
    Column("id", Integer(), primary_key=True),
    Column("user_id", Integer(), ForeignKey("user.id"), nullable=False),
    Column("x", Float(), primary_key=True),
    Column("y", Float(), primary_key=True),
    Column("timestamp", Float(), primary_key=True)
)