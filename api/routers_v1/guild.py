from fastapi import APIRouter

router = APIRouter()

@router.get('/v1/guild/{guild_id}/settings', tags=['guild'])
async def getGuildSettings(guild_id):
    return {'guild_settings': []}

@router.put('/v1/guild/{guild_id}/settings', tags=['guild'])
async def putGuildSettings(guild_id):
    return {'guild_settings': []}

@router.get('/v1/guild/{guild_id}/role', tags=['guild'])
async def getGuildRole(guild_id):
    return {'guild_roles': []}