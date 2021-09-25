from flask import request, make_response

from backend.app import app
from backend.utils.utils import create_new_user, get_user_by_cookie, add_eye_data, get_user_by_id, \
    get_eye_data_by_user_id


@app.route('/eye_data', methods=['GET'])
def get_eye_data():
    """
        get eye data
        ---
        parameters:
          - name: user_id
            in: query
            type: int
            required: false
          - name: time_limit
            in: query
            type: int
            required: false
        responses:
          200:
            description: Return eye data
    """
    user_id = request.args["user_id"]
    user = get_user_by_id(user_id)
    if not user:
        return "User is not found", 404

    eye_data = get_eye_data_by_user_id(user.id)
    print(user)


@app.route('/send_eye_data', methods=['POST'])
def send_eye_data():
    """
        send eye data
        ---
        consumes:
          - application/json
        parameters:
          - name: eye_data
            in: body
            required: true
        responses:
          201:
            description: Data is added successfully
    """
    user_cookie = request.cookies.get("user_cookie")
    user = get_user_by_cookie(user_cookie)
    change_cookie_flag = False
    if not user:
        user = create_new_user()
        change_cookie_flag = True

    eye_data = request.json
    add_eye_data(user.id, eye_data)

    response = make_response("Data is added successfully", 201)

    if change_cookie_flag:
        response.set_cookie("user_cookie", user.cookie)

    return response
