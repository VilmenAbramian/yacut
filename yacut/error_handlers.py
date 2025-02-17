from http import HTTPStatus
from flask import jsonify, render_template

from . import app


class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'message': self.message}


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(415)
def unsupported_media_type(error):
    """Обработчик ошибки 415, возвращает JSON"""
    response = jsonify(
        {'message': 'Отсутствует тело запроса'}
    )
    response.status_code = 400
    return response


@app.errorhandler(InvalidAPIUsage)
def api_exception(error):
    """Обработчик кастомных API-ошибок"""
    return jsonify(error.to_dict()), error.status_code