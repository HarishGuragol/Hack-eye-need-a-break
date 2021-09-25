from contextlib import contextmanager

from sqlalchemy.orm import Session


def config_session_creator(engine):
    @contextmanager
    def create_session():
        """Provide a transactional scope around a series of operations."""
        session = Session(bind=engine)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    return create_session


