import re
from flask import Flask, redirect, request, jsonify, make_response, Response
import flask
from flask_cors import CORS
from service.auth import AuthService
from service.login import LoginService
from service.token_factory import TokenService
from models.requestinfo import RequestInfo
from utils.validator import Validator, LoginValidator, RegistrationValidator
from service.register import RegistrationService
from models.result import Result
import utils.messages as messages
from exceptions.exceptions import InvalidRequestException
from dbengine import InputQuery, OutputQuery
from config import DB_INIT

app = Flask(__name__)
app.config.from_object('config')
CORS(app, supports_credentials=True)


def service_manager(auth_service: AuthService) -> Response:
    try:
        auth_service.perform_checks()
        auth_service.sign_user()
    except InvalidRequestException as err:
        auth_service.result.failed(err.code, err.message)
    except Exception as err:
        print(err)
        auth_service.result.failed(500, messages.GENERIC_ERROR)

    response = make_response(
        jsonify(auth_service.result.__dict__),
        auth_service.result.status_code)

    return response


@app.route('/login', methods=['POST'])
def login():
    result = Result()
    request_info = RequestInfo(dict(request.json))
    login_validator = LoginValidator(request_info)
    token_service = TokenService()
    login_service = LoginService(
        request_info, login_validator, result, token_service)

    response = service_manager(login_service)

    if dict(response.json).get('status_code') == 200:
        cookie = dict(
            key=messages.COOKIE_KEY,
            value=dict(response.json).get("body")["token"],
            max_age=None,
            expires=None,
            domain=None,
            secure=True,
            samesite="None",
            httponly=True
        )
    response.set_cookie(**cookie)

    return response

@app.route('/register', methods=['POST'])
def register():
    result = Result()
    request_info = RequestInfo(dict(request.json))
    registration_validator = RegistrationValidator(request_info)
    registration_service = RegistrationService(
        request_info, registration_validator, result)

    return service_manager(registration_service)


@app.route('/validate', methods=['POST'])
def validate():
    result = Result()
    token_service = TokenService()
    token_service.validate(request, result)
    return make_response(
        jsonify(result.__dict__),
        result.status_code)


if __name__ == '__main__':
    InputQuery().execute(DB_INIT)
    app.run(debug=True)
