from fastapi import APIRouter
from fastapi.params import Depends

from src.api.v1.services.user import UsersService
from src.auth.utils import hash_password
from src.schemas.token import TokenInfo
from src.schemas.user import CreateUserRequest, UserDB
from src.auth import utils as auth_utils

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

@router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(
        user: UserDB = Depends(auth_utils.validate_auth_user),
):
    jwt_payload = {
        'sub': user.full_name,
        'email': user.email,
        'username': user.full_name,
    }
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer"
    )


@router.get('/users/me')
def auth_user_check_self_info(
        user: UserDB = Depends(auth_utils.get_current_auth_user),
        payload: dict = Depends(auth_utils.get_current_token_payload),
):
    iat = payload.get('iat')
    return {
        'username': user.full_name,
        'email': user.email,
        'logged_in_at': iat
    }


@router.post('')
async def add_user(
    user: CreateUserRequest,
    service: UsersService = Depends(),
):
    user.password = hash_password(user.password).decode('utf-8')
    user_id = await service.add_user(user)
    return {'user_id': user_id}


@router.get('')
async def get_users(
    service: UsersService = Depends(),
):
    users = await service.get_users()
    return users
