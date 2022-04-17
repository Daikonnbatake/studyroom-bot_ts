from fastapi import APIRouter

router = APIRouter()

@router.get('/user/{user_id}/settings', tags=['user'])
async def getUserSettings(user_id):
    return {'user_settings': []}

@router.put('/user/{user_id}/settings', tags=['user'])
async def putUserSettings(user_id):
    return {'err': 0}