from flask import request, Blueprint
import json
from usecase.usecase import Usecase
from botocore.exceptions import ClientError

user_controller = Blueprint("user", __name__)

usecase = Usecase()

ERROR_MSG = "Account creation failed"


def to_ok_response(body):
    return None


def to_ng_response(body):
    return None


# def authorization():
#     try:
#         auth_header = request.headers.get("Authorization", "")


class CRUD:
    @user_controller.route("/signup", methods=["POST"])
    def create():
        try:
            user_data = json.loads(request.get_data().decode())
        except:
            return {"message": ERROR_MSG, "cause": "required user_id and password"}, 400

        try:
            response, status_code = usecase.create(user_data)
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "ConditionalCheckFailedException":
                cause_msg = "already same user_id is used"
                return {"message": ERROR_MSG, "cause": cause_msg}, 400
        except Exception:
            cause_msg = "system error"
            return {"message": ERROR_MSG, "cause": cause_msg}, 500

        return {
            "message": "Account successfully created",
            "user": response.get("user"),
        }, status_code

    @user_controller.route("/users/<user_id>", methods=["GET"])
    def read(user_id):
        try:
            response, status_code = usecase.read(user_id)
        except Exception:
            err_msg = "system error"
            return {"message": err_msg}, 500

        # Authorization ヘッダでの認証を行う

        if status_code == 404:
            return {"message": "No User found"}, 404

        data = json.dumps(response)
        return data, status_code