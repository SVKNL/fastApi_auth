from fastapi import APIRouter
from fastapi.params import Depends

from src.api.v1.services.user import UsersService
from src.schemas.user import CreateUserRequest, UserFilterSchema

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.post('')
async def add_user(
    user: CreateUserRequest,
    service: UsersService = Depends(),
):
    user_id = await service.add_user(user)
    return {'user_id': user_id}


@router.get('')
async def get_users(
    filter: UserFilterSchema = Depends(),
    service: UsersService = Depends(),
):
    users = await service.get_users(filter)
    return users
