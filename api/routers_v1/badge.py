import os, sys; sys.path.append(os.pardir)

from utilities.db_access import DBAccess as db
from my_typing.response import Badges, PutResponse
from my_typing.request_body import PutBadgeSet
from fastapi import APIRouter

router = APIRouter()

# バッジの一覧を取得する
@router.get('/v1/badges/list', tags=['badges'], response_model=Badges)
async def getBadge():
    
    # 戻り値の定義とDBからbadge一覧を取得
    ret = Badges()
    res = db.select('mst_badge')

    # エラー時の処理
    if res == 'error': ret.error.error('failed to connect database.')
    
    # 成功時の処理
    else:
        ret.error.success()
        for i in res: ret.appendBadge(i['id'], i['name'], i['description'])

    return ret


# 現在所持しているバッジを取得する
@router.get('/v1/badges/acquired/{user_id}', tags=['badges'], response_model=Badges)
async def getBadgeAcquired(user_id):

    # 戻り値の定義とDBから各種データを取得
    ret = Badges()
    res = db.select('users', ['id', 'badge_acquired'], 'id = %s', [user_id])
    badges = db.select('mst_badge', ['*'])

    # エラー時の処理
    if res == 'error' or badges == 'error': ret.error.error()

    # 成功時の処理
    else:
        ret.error.success()

        # bit シフトで取得済みバッジのフラグを取って取得済みバッジ一覧を作成
        for i in range(26):
            if res['badge_acquired'] >> i & 1:
                badge = badges[i]
                ret.appendBadge(badge['id'], badge['name'], badge['description'])

    return ret


# 現在装備しているバッジを取得する
@router.get('/v1/badges/equipped/{user_id}', tags=['badges'], response_model=Badges)
async def getBadgeEqyupped(user_id):
    
    # 戻り値の定義とDBから各種データを取得
    ret = Badges()
    res = db.select('users', ['id', 'badge_equipe_1', 'badge_equipe_2', 'badge_equipe_3'], 'id = %s', [user_id])
    badges = db.select('mst_badge', ['*'])
    
    # エラー時の処理
    if res == 'error' or badges == 'error': ret.error.error('user_id "%s" is not exists.' % user_id)
    
    # 成功時の処理
    else:
        ret.error.success()

        for i in range(1, 4):
            badgeId = res['badge_equipe_%d' % i]    # badge_equipe_1/2/3 のそれぞれの項目(バッジのID)を取得する
            badge = badges[badgeId-1]               # DBでは 1 index なので 0 index に直す
            ret.appendBadge(badge['id'], badge['name'], badge['description'])

    return ret

# バッジを装備する
@router.put('/v1/badges/set/{user_id}', tags=['badges'], response_model=PutResponse)
async def badgeSet(user_id: int, badges: PutBadgeSet):
    ret = PutResponse()
    res = db.update('users', ['badge_equipe_1', 'badge_equipe_2', 'badge_equipe_3'], [badges.badge_1, badges.badge_2, badges.badge_3], 'id = %s', [user_id])
    
    if res == 'error': ret.error.error('failed update to user_id "%s".' % user_id)
    else: ret.error.success()
    return ret