import json
from fastapi import FastAPI
from fastapi.responses import FileResponse

from routers import badge, guild, ranking, studytime, user

from utilities.db_access import DBAccess as db

with open('/usr/srb3/source/conf.json', 'r', encoding='utf8') as f:
    conf = json.load(f)['mysql']
    db.host(conf['host'])
    db.port(conf['port'])
    db.user(conf['user'])
    db.password(conf['password'])
    db.database(conf['db'])

print(db.select('mst_roles', ['id', 'name'], 'name=%s', ('灰筆',)))
print(db.insert('test', ['number', 'string'], ['999', 'abc']))

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