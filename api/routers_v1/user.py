from fastapi import APIRouter

router = APIRouter()

@router.get('/v1/user/{user_id}/settings', tags=['user'])
async def getUserSettings(user_id):
    return {'user_settings': []}

@router.post('/v1/user/add')
async def postUserAdd():
    return {'err': 0}

@router.put('/v1/user/{user_id}/settings', tags=['user'])
async def putUserSettings(user_id):
    return {'err': 0}