from models import User


class UserController:
    current_user: User

    @property
    @classmethod
    def user(cls):
        return cls.current_user

    @classmethod
    def create(cls, email, category) -> User:
        user = User.create(email, category)
        current_user = user
        return current_user

    @classmethod
    def update(cls, id, username, email) -> User:
        user = User.find_by_id(id)
        user.email = email
        user.username = username
        user.update()
        return user

    @classmethod
    def delete(cls) -> str:
        user = User.find_by_id(cls.current_user.id)
        user.delete()
        return f"User deleted successfully: {user.email}"

    @classmethod
    def find_by_email(cls, email) -> User:
        user = User.find_by_email(email)
        current_user = user
        return current_user

    @classmethod
    def find_by_id(cls, id) -> User:
        user = User.find_by_id(id)
        current_user = user
        return current_user

    @classmethod
    def find_all(cls) -> list:
        users = User.find_all()
        return users
