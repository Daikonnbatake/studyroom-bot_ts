from fastapi import APIRouter

router = APIRouter()

# guild 新規登録
@router.post('/v1/guilds/add', tags=['guilds'])
async def postGuildAdd():
    return {'err': []}

# guild の設定云々について
#   自習室のチャンネル
#   アナウンス用のチャンネル

# guild の設定を取得
@router.get('/v1/guilds/{guild_id}/settings', tags=['guilds'])
async def getGuildSettings(guild_id):
    return {'guild_settings': []}

# guild の設定を更新
@router.put('/v1/guilds/{guild_id}/settings', tags=['guilds'])
async def putGuildSettings(guild_id):
    return {'guild_settings': []}