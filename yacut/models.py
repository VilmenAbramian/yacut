from datetime import datetime
import random


from yacut import db
from settings import USER_LINK_LIMIT, VALID_SYMBOLS



class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        ...

    def from_dict(self, data):
        ...

    def get_unique_short_id(self, lenght=6):
        while True:
            short_link = ''.join(random.choice(VALID_SYMBOLS) for _ in range(lenght))
            if not URLMap.query.filter_by(short=short_link).first():
                return short_link

    def is_valid_short_id(self, short_id):
        if len(short_id) > USER_LINK_LIMIT:
            return False
        for value in short_id:
            if value not in VALID_SYMBOLS:
                return False
        return True