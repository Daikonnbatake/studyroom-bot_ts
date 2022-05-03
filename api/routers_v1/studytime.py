from fastapi import APIRouter

router = APIRouter()

@router.get('/v1/studytime/{user_id}', tags=['studytime'])
async def getStudytime(user_id):
    return {'time': []}

@router.post('/v1/studytime/{user_id}', tags=['studytime'])
async def postStudytime(user_id):
    return