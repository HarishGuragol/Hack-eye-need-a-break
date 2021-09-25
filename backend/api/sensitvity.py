from flask import request, make_response

from backend.app import app
from backend.utils.utils import get_user_by_cookie, create_new_user, create_new_sensitivity, get_sensitivity_by_user_id, \
    set_sensitivity


@app.route('/send_sensitivity', methods=['POST'])
def send_sensitivity():
    """
        send sensitivity
        ---
        consumes:
          - application/json
        parameters:
          - name: data
            in: body
            required: true
        responses:
          200:
            description: Зачем тебе переводчик? =)
    """
    user_cookie = request.cookies.get("user_cookie")
    user = get_user_by_cookie(user_cookie)
    change_cookie_flag = False
    if not user:
        user = create_new_user()
        change_cookie_flag = True

    data = request.json
    if get_sensitivity_by_user_id(user.id):
        set_sensitivity(user.id, data["value"])
    else:
        create_new_sensitivity(user.id, data["value"])

    response = make_response("Data is added successfully", 201)

    if change_cookie_flag:
        response.set_cookie("user_cookie", user.cookie)

    return response