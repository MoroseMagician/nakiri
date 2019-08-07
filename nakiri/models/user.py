from nakiri.models.db import db
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import jwt
import os


class User(db.Model):
    __table_args__ = (
        db.UniqueConstraint('username'),
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def add(self):
        """ Add the user to the database """
        # Hash and salt the password first
        self.password = generate_password_hash(
            self.password,
            'pbkdf2:sha512:50000'
        )
        db.session.add(self)
        db.session.commit()

    def generate_token(self) -> str:
        """ Generate a JWT token for the user """
        payload = {
            'user': self.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=7)
        }
        secret = os.environ['NAKIRI_KEY']

        # Make sure the key is properly set
        assert(len(secret) >= 32)

        token = jwt.encode(payload, secret, algorithm='HS256')
        return token.decode('utf-8')

    def __repr__(self) -> str:
        return f"<User({self.username})>"
