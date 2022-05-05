from fastapi import APIRouter

router = APIRouter()

# 自習時間を日単位の区間で取得
@router.get('/v1/studytime/{user_id}', tags=['studytime'])
async def getStudytime(user_id):
    return {'time': []}

# 入退室を記録
@router.post('/v1/studytime/{user_id}', tags=['studytime'])
async def postStudytime(user_id):
    return