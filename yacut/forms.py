from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length

from . import validators
from settings import USER_LINK_LIMIT, VALID_SYMBOLS


class LinkForm(FlaskForm):
    original_link = URLField(
        'Добавьте укорачиваемую ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            validators.URL(message='Некорректный URL'),
            Length(1, 256)
        ]
    )
    custom_id = URLField(
        'Добавьте свой вариант короткой ссылки',
        validators=(
            validators.Optional(),
            validators.Length(
                max=USER_LINK_LIMIT,
                message='Слишком длинная ссылка'
            ),
            validators.AllOf(
                values=VALID_SYMBOLS,
                message='Разрешены только латиница и цифры'
            )
        )
    )
    submit = SubmitField('Создать ссылку')