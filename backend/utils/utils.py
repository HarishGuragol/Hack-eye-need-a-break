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
    free_index = last_free_id(EyeData)
    eye_data = [{"user_id": user_id, **eye_item} for eye_item in eye_data]

    for eye_item in eye_data:
        eye_item["id"] = free_index
        free_index += 1

    with create_session() as sess:
        while True:
            insert_data = eye_data[:50]
            if not insert_data:
                break

            insert_eye_data = EyeData.insert().values(insert_data)
            sess.execute(insert_eye_data)
            eye_data = eye_data[50:]




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


def last_free_id(table):
    with create_session() as sess:
        data = sess.query(EyeData).order_by(table.c.id.desc()).first()

    if not data:
        index_free = 1
    else:
        index_free = data[0] + 1

    return index_free