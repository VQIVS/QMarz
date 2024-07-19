from app.models.user import User
from app import db


class UserRepository:
    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def get_by_username(self, user_id):
        return User.query.filter_by(user_id=user_id).first()

    def create(self, user_id):
        if self.get_by_username(user_id):
            raise ValueError("User with this username already exists")

        new_user = User(user_id=user_id)
        db.session.add(new_user)
        db.session.commit()
