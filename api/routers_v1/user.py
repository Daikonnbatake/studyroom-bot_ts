import os, sys; sys.path.append(os.pardir)

from utilities.db_access import DBAccess as db
from my_typing.request_body import PostUserAdd
from my_typing.response import ResponseErrorCode
from fastapi import APIRouter

router = APIRouter()

# ユーザーを新規登録
@router.post('/v1/users/add', tags=['users'], response_model=ResponseErrorCode)
async def postUserAdd(user_id: PostUserAdd):
    ret = ResponseErrorCode(error_code=0, message='success')
    res = db.insert('users', ['id'], [user_id])
    if res == 'error':
        ret.error_code = 1
        ret.message = 'userid "%s" is exist.' % user_id
    return ret

# 自習ランクを取得
@router.get('/v1/users/{user_id}/rank', tags=['users'])
async def getUserRank(user_id):
    return {'user_rank': []}

# 自習レベルを取得
@router.get('/v1/users/{user_id}/level', tags=['users'])
async def getUserRank(user_id):
    return {'user_level': []}

# ユーザーの設定情報を取得
@router.get('/v1/users/{user_id}/settings', tags=['users'])
async def getUserSettings(user_id):
    return {'user_settings': []}

# ユーザーの設定情報を更新
@router.put('/v1/users/{user_id}/settings', tags=['users'])
async def putUserSettings(user_id):
    return {'err': 0}