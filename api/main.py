from fastapi import FastAPI
from fastapi.responses import FileResponse

from routers import badge, guild, ranking, studytime, user

app = FastAPI(
    title = '自習室API',
    description = '自習室botのバックグラウンド',
    version = '0.1.0'
)

# favicon を返すための設定
@app.get('/favicon.ico')
async def getFavicon(): return FileResponse('./favicon.ico')

# 各種エンドポイント
app.include_router(badge.router)
app.include_router(guild.router)
app.include_router(ranking.router)
app.include_router(studytime.router)
app.include_router(user.router)