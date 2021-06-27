from flask import Flask, request
from controller.controller import user_controller
import awsgi

app = Flask(__name__)
app.register_blueprint(user_controller)


def lambda_handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")