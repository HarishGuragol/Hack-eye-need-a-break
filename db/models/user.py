from sqlalchemy import Integer, Column, String, Table

from db.meta import metadata

User = Table("user", metadata,
    Column("id", Integer(), primary_key=True, autoincrement=True),
    Column("cookie", String(32), nullable=True),
    Column("first_name", String(40), nullable=True),
    Column("last_name", String(40), nullable=True),
    Column("email", String(60), nullable=True),
)
