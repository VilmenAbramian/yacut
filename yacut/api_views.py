from flask import jsonify, request, url_for

from . import app, db
from settings import USER_LINK_LIMIT
from . import validators
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def new_short_url():
    """Создание новой короткой ссылки"""
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    original_url = data.get('url')
    if original_url is None:
        return jsonify({'message': '"url" является обязательным полем!'}), 400
    short_link = data.get('custom_id')
    if short_link:
        validators.len_validation(
            short_link,
            InvalidAPIUsage('Указано недопустимое имя для короткой ссылки'),
            max=USER_LINK_LIMIT
        )
        validators.symbols_validation(
            short_link,
            InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        )
        if URLMap.query.filter_by(short=short_link).first():
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
    else:
        short_link = URLMap.get_unique_short_id()

    if short_link is None:
        raise InvalidAPIUsage('Не удалось сгенерировать короткую ссылку!')

    url_map = URLMap(original=original_url, short=short_link)
    db.session.add(url_map)
    db.session.commit()

    response_dict = {
        'short_link': url_for(
            'redirect_short_link', short_id=short_link, _external=True
        ),
        'url': original_url
    }

    return jsonify(response_dict), 201


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def api_redirect_short_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)

    response_dict = {
        'url': url_map.original
    }
    return response_dict, 200
