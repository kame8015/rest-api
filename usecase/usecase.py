from repository.user_dynamodb import DynamoDB
from domain.user import User
from app_config import REGION_NAME, DYNAMODB_ENDPOINT, TABLE_NAME
import re


def is_valid_user_id(user_id):
    pattern = "[a-zA-Z0-9]"
    if not re.match(pattern, user_id):
        return False
    return True


def is_valid_password(password):
    pattern = "\A[a-z\d]\Z(?i)"
    if not re.match(pattern, password):
        return False
    return True


class Usecase:
    def __init__(self):
        self.dynamodb = DynamoDB(
            region_name=REGION_NAME, endpoint=DYNAMODB_ENDPOINT, table_name=TABLE_NAME
        )

    def create(self, user_data):
        # 必須項目の存在チェック
        if (user_id := user_data.get("user_id")) is None or (password := user_data.get("password")) is None:
            cause_msg = "required user_id and password"
            return cause_msg, 400

        # 文字種のチェック
        if not (is_valid_user_id(user_id) or is_valid_password(password)):
            cause_msg = "invalid pattern user_id and password"
            return cause_msg, 400

        # 値の長さのチェック
        if (
            len(user_id) < 6
            or 20 < len(user_id)
            or len(password) < 8
            or 20 < len(password)
        ):
            cause_msg = "invalid length user_id and password"
            return cause_msg, 400

        user = User(user_id, password)
        self.dynamodb.create(user)
        return {"user": {"user_id": user.user_id, "nickname": user.user_id}}, 200
