from nakiri.models.db import db
from datetime import datetime, timedelta
import jwt
import os


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, nullable=False, index=True)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, user_id) -> None:
        """ Generate a JWT token """
        payload = {
            'user': user_id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=7)
        }
        secret = os.environ['NAKIRI_KEY']

        # Make sure the key is properly set
        assert(len(secret) >= 32)

        token = jwt.encode(payload, secret, algorithm='HS256')
        self.token = token.decode('utf-8')

    def add(self) -> None:
        """ Add the token to the database """
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        """ Soft-delete a token """
        self.deleted = True
        db.session.commit()
