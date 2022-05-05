import os, sys; sys.path.append(os.pardir)

from utilities.db_access import DBAccess as db
from my_typing.request_body import PostUserAdd
from my_typing.response import User, PostResponse
from fastapi import APIRouter

router = APIRouter()

# ユーザーを新規登録
@router.post('/v1/users/add', tags=['users'], response_model=PostResponse)
async def postUserAdd(user_id: PostUserAdd):

    # 戻り値の定義とDBにinsert
    ret = PostResponse
    res = db.insert('users', ['id'], [user_id])
    
    # エラー時の処理
    if res == 'error': ret.error.error('userid "%s" is exist.' % user_id)
    
    # 成功時の処理
    else: ret.error.success()

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
@router.get('/v1/users/{user_id}/settings', tags=['users'], response_model=User)
async def getUserSettings(user_id):

    # 戻り値の定義とDBからデータ取得
    ret = User()
    res = db.select('users',['id', 'privacy_data', 'privacy_rank'], 'id = %s', [user_id])

    # エラー時の処理
    if res == 'error': ret.error.error('user_id "%s" is not exists.' % user_id)

    # 成功時の処理
    else:
        ret.error.success()

        ret.body.id = res['id']
        ret.body.settings.privacy_data = bool(res['privacy_data'])
        ret.body.settings.privacy_rank = bool(res['privacy_rank'])

    return ret


# ユーザーの設定情報を更新
@router.put('/v1/users/{user_id}/settings', tags=['users'])
async def putUserSettings(user_id):
    return {'err': 0}