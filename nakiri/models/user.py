from nakiri.models.db import db
from werkzeug.security import generate_password_hash
from datetime import datetime


class User(db.Model):
    __table_args__ = (
        db.UniqueConstraint('username'),
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def add(self) -> None:
        """ Add the user to the database """
        # Hash and salt the password first
        self.password = generate_password_hash(
            self.password,
            'pbkdf2:sha512:50000'
        )
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f"<User({self.username})>"
