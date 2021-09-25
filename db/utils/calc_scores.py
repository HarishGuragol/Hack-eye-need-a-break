import time
import numpy as np
from backend.session import create_session
from backend.utils.utils import create_score
from db.models import EyeData, Score, User
from distraction_classification.score import score_variance

range_time = 60 * 5
check_everytime_step = 60


def calc_score_for_one_time(user_id, timestamp):
    left = timestamp - range_time
    right = timestamp

    with create_session() as sess:
        score = (
            sess.query(Score)
            .filter(Score.c.user_id == user_id)
            .filter(Score.c.timestamp == right)
            .one_or_none()
        )

        if score:
            return

        eye_data = (
            sess.query(EyeData)
            .filter(EyeData.c.user_id == user_id)
            .filter(EyeData.c.timestamp > left)
            .filter(EyeData.c.timestamp < right)
            .order_by(EyeData.c.timestamp)
            .all()
        )

        if not eye_data:
            return

        eye_data_arr = np.array(list([
            [eye_item[2], eye_item[3], int(eye_item[4])]
            for eye_item in eye_data
        ]))
        try:
            score = score_variance(eye_data_arr, 1920, 1080)
        except:
            pass

        if np.isnan(score):
            return

        create_score(user_id, score, timestamp)


def calc_score_for_all_time(user_id):
    with create_session() as sess:
        most_old_eye_data = (
            sess.query(EyeData)
            .filter(EyeData.c.user_id == user_id)
            .order_by(EyeData.c.timestamp)
            .first()
        )

        if not most_old_eye_data:
            return

    dt = most_old_eye_data.timestamp
    while time.time() > dt:
        calc_score_for_one_time(user_id, dt)
        dt += check_everytime_step


def calc_score_for_all_users():
    with create_session() as sess:
        users = sess.query(User).all()
        for user in users:
            calc_score_for_all_time(user[0])


def get_dash_data(user_id):
    with create_session() as sess:
        scores = (
            sess.query(Score)
            .filter(Score.c.user_id == user_id)
            .order_by(Score.c.timestamp)
            .all()
        )
        s = [score[2] for score in scores]
        dt = [score[3] for score in scores]
    return s, dt


if __name__ == '__main__':
    while True:
        calc_score_for_all_users()