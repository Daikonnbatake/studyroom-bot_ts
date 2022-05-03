import os, sys
sys.path.append(os.pardir)

from utilities.db_access import DBAccess as db
from fastapi import APIRouter

router = APIRouter()

# バッジの一覧を取得する
@router.get('/v1/badges/list', tags=['badges'])
async def getBadge():
    # DBからバッジのマスタを持ってくる
    result = db.select('mst_badge')
    return {'badges': result}

# 現在所持しているバッジを取得する
@router.get('/v1/badges/acquired/{user_id}', tags=['badges'])
async def getBadgeAcquired(user_id):
    return {'badges': []}

# 現在装備しているバッジを取得する
@router.get('/v1/badges/equipped/{user_id}', tags=['badges'])
async def getBadgeEqyupped(user_id):
    return {'badges': []}

# バッジを装備する
@router.put('/v1/badges/set/{user_id}', tags=['badges'])
async def badgeSet(user_id):
    return {'err': '0'}