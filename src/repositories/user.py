from src.models.task import User
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository[User]):
    model = User
