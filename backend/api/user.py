from flask import make_response, jsonify

from backend.app import app
from backend.utils.utils import get_all_users


@app.route("/users")
def get_all_users_api():
    """
        get all users
        ---
        responses:
          200:
            description: Return all users
    """
    users = get_all_users()
    users = list([{
        "id": user[0],
        "first_name": user[2],
        "last_name": user[3],
        "email": user[4],
    } for user in users])
    return jsonify(users)
