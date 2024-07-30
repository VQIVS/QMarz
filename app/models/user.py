from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<User {self.user_id}>"
