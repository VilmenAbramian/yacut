from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from settings import USER_LINK_LIMIT


class LinkForm(FlaskForm):
    original_link = URLField(
        'Добавьте укорачиваемую ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256)
        ]
    )
    custom_id = URLField(
        'Добавьте свой вариант короткой ссылки',
        validators=[Length(1, USER_LINK_LIMIT), Optional()]
    )
    submit = SubmitField('Создать ссылку')