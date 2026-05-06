import uuid
from src.domain.entities import User
from src.application.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, name: str, email: str, phone: str) -> User:
        user = User(id=str(uuid.uuid4()), name=name, email=email, phone=phone)
        return self.user_repository.save(user)

class GetUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> User | None:
        return self.user_repository.get_by_id(user_id)

class GetAllUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> list[User]:
        return self.user_repository.get_all()

class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str, name: str, email: str, phone: str) -> User | None:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return None
        user.name = name
        user.email = email
        user.phone = phone
        return self.user_repository.update(user)

class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> bool:
        return self.user_repository.delete(user_id)
