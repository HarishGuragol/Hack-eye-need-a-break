import time

from backend.session import create_session
from db.models import User, EyeData
import secrets


def create_new_user(first_name=None, last_name=None, email=None, cookie=None):
    if cookie is None:
        cookie = secrets.token_urlsafe(24)

    with create_session() as sess:
        insert_user = User.insert().values(
            cookie=cookie,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        sess.execute(insert_user)
        new_user = sess.query(User).filter(User.c.cookie == cookie).one_or_none()
    return new_user


def get_all_users():
    with create_session() as sess:
        users = sess.query(User).all()
    return users


def get_user_by_cookie(cookie):
    with create_session() as sess:
        user = sess.query(User).filter(User.c.cookie == cookie).one_or_none()
    return user


def get_user_by_id(user_id):
    with create_session() as sess:
        user = sess.query(User).filter(User.c.id == user_id).one_or_none()
    return user


def add_eye_data(user_id, eye_data):
    eye_data = [{"user_id": user_id, **eye_item} for eye_item in eye_data]
    with create_session() as sess:
        insert_eye_data = EyeData.insert().values(eye_data)
        sess.execute(insert_eye_data)


def get_eye_data_by_user_id(user_id, limit_time=60 * 10):
    time_filter_value = time.time() - limit_time
    with create_session() as sess:
        eye_data = (
            sess.query(EyeData)
            .filter(EyeData.c.user_id == user_id)
            .filter(EyeData.c.timestamp > time_filter_value)
            .order_by(EyeData.c.timestamp)
            .all()
        )
    return eye_data
