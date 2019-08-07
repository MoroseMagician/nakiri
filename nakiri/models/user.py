from nakiri.models.db import db
from werkzeug.security import generate_password_hash


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

    def __repr__(self):
        return f"<User({self.username})>"
