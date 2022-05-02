import os, sys
sys.path.append(os.pardir)

from utilities.db_access import DBAccess
from fastapi import APIRouter

router = APIRouter()

# バッジの一覧を取得する
@router.get('/badge/list', tags=['badge'])
async def getBadge():
    
    # DBからバッジのマスタを持ってくる
    result = DBAccess().exec([['', '']])
    return {'badges': []}

@router.get('badge/acquired/{user_id}', tags=['badge'])
async def getBadgeAcquired(user_id):
    return {'badges': []}

@router.get('badge/equipped/{user_id}', tags=['badge'])
async def getBadgeEqyupped(user_id):
    return {'badges': []}

@router.put('badge/set/{user_id}', tags=['badge'])
async def badgeSet(user_id):
    return {'err': '0'}