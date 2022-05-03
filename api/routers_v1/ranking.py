from fastapi import APIRouter

router = APIRouter()

@router.get('/v1/ranking/global', tags=['ranking'])
async def getRankingGlobal():
    return {'ranking': []}

@router.get('/v1/ranking/local/{guild_id}', tags=['ranking'])
async def getLocalRanking(guild_id):
    return {'ranking': []}