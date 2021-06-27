import boto3
from domain.user import User


class DynamoDB:
    def __init__(self, region_name, endpoint, table_name):
        self.dynamodb = boto3.resource(
            service_name="dynamodb", region_name=region_name, endpoint_url=endpoint
        )
        self.user_table = self.dynamodb.Table(table_name=table_name)

    def create(self, user):
        response = self.user_table.put_item(
            Item={
                "user_id": user.user_id,
                "password": user.password,
                "nickname": user.user_id,
            },
            ConditionExpression="attribute_not_exists(#user_id)",
            ExpressionAttributeNames={"#user_id": "user_id"},
        )

        return response

    def read(self, user_id):
        response = self.user_table.get_item(Key={"user_id": user_id})

        if (response_user := response.get("Item")) is None:
            return None

        user = User(
            response_user.get("user_id"),
            response_user.get("nickname"),
            response_user.get("comment"),
        )

        return user