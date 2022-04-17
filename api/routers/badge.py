import imp
from fastapi import APIRouter

router = APIRouter()

@router.get('/badge/list', tags=['badge'])
async def getBadge():
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