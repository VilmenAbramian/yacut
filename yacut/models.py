from datetime import datetime
from random import choices

from flask import url_for

from .error_handlers import ShortLinkGenerationError
from yacut import db
from settings import (BAD_SHORT, GENERATION_FAIL,
                      MAX_ATTEMPTS, MAX_ORIGINAL_LENGTH,
                      SHORT_EXIST, SHORT_LENGTH,
                      USER_LINK_LIMIT, VALID_SYMBOLS)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def get_unique_short():
        for _ in range(MAX_ATTEMPTS):
            short = ''.join(choices(VALID_SYMBOLS, k=SHORT_LENGTH))
            if not URLMap.get(short):
                return short
        raise ShortLinkGenerationError(GENERATION_FAIL)

    @staticmethod
    def get(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def create(original, short=None):
        if short:
            if ((len(short) > USER_LINK_LIMIT) or
                    any(char not in VALID_SYMBOLS for char in short)):
                raise ValueError(BAD_SHORT)
            if URLMap.get(short):
                raise ValueError(SHORT_EXIST)
        else:
            short = URLMap.get_unique_short()
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map

    def short_link(self):
        return url_for('redirect_short_link', short=self.short, _external=True)

    def to_dict(self, original_only=False):
        if original_only:
            return dict(url=self.original)
        return dict(url=self.original, short_link=self.short_link())

    def is_valid_short(self, short_id):
        if len(short_id) > USER_LINK_LIMIT:
            raise ValueError(BAD_SHORT)
        for value in short_id:
            if value not in VALID_SYMBOLS:
                raise ValueError(BAD_SHORT)
        return True