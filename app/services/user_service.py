from app.repositories.user_repository import UserRepository

user_repo = UserRepository()


def create_user(user_id):
    return user_repo.create(user_id)
