import random
import time

from backend.session import create_session
from backend.utils.utils import create_new_user, add_eye_data
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
        "timestamp": time.time() + random.randint(0, 50) - 50
    } for _ in range(1000)]

    with create_session() as sess:
        user = sess.query(User).filter(User.c.email == test_user["email"]).one_or_none()
        if not user:
            user = create_new_user(
                first_name=test_user["first_name"],
                last_name=test_user["last_name"],
                email=test_user["email"],
            )
        add_eye_data(user.id, test_eye_data)
