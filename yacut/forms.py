from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import (MAX_ORIGINAL_LENGTH, MIN_ORIGINAL_LENGTH,
                      SHORT_PATTERN, USER_LINK_LIMIT)


class LinkForm(FlaskForm):
    original_link = URLField(
        'Добавьте укорачиваемую ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректный URL'),
            Length(MIN_ORIGINAL_LENGTH, MAX_ORIGINAL_LENGTH)
        ]
    )
    custom_id = URLField(
        'Добавьте свой вариант короткой ссылки',
        validators=(
            Optional(),
            Length(
                max=USER_LINK_LIMIT,
                message='Слишком длинная ссылка'
            ),
            Regexp(SHORT_PATTERN, message='Разрешены только латиница и цифры'),
        )
    )
    submit = SubmitField('Создать ссылку')
