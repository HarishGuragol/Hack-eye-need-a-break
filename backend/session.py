from db.engine import engine
from db.session import config_session_creator

create_session = config_session_creator(engine=engine)
