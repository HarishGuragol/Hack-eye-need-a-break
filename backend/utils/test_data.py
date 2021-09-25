import random
import time

from backend.session import create_session
from backend.utils.utils import create_new_user, add_eye_data, get_sensitivity_by_user_id, set_sensitivity, \
    create_new_sensitivity
from db.models import User


def add_test_data():
    test_user = {
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "test@test.com",
    }

    test_eye_data = [{
        "x": random.randint(0, 100),
        "y": random.randint(0, 100),
        "timestamp": time.time() + random.randint(0, 1000) - 1000
    } for _ in range(20000)]

    with create_session() as sess:
        user = sess.query(User).filter(User.c.email == test_user["email"]).one_or_none()
        if not user:
            user = create_new_user(
                first_name=test_user["first_name"],
                last_name=test_user["last_name"],
                email=test_user["email"],
            )
        add_eye_data(user.id, test_eye_data)

    if not get_sensitivity_by_user_id(user.id):
        create_new_sensitivity(user.id, 0.6)
