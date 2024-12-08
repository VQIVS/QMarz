from app.models.user import User
from app import db


class UserRepository:
    def create(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            return user
        new_user = User(user_id=user_id)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_by_user_id(self, user_id):
        return User.query.filter_by(user_id=user_id).first()

    def get_all_users(self):
        return User.query.all()