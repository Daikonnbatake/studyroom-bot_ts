import os, sys

from pymysql import Timestamp; sys.path.append(os.pardir)

from utilities.db_access import DBAccess as db
from my_typing.request_body import PostVoiceActivity
from my_typing.response import PostResponse
from fastapi import APIRouter

router = APIRouter()

# 自習時間を日単位の区間で取得
@router.get('/v1/studytime/{user_id}', tags=['studytime'])
async def getStudytime(user_id):
    return {'time': []}

# 入退室を記録
@router.post('/v1/studytime/{user_id}', tags=['studytime'], response_model=PostResponse)
async def postStudytime(user_id: int, voiceActivity: PostVoiceActivity):
    # 戻り値の定義
    ret = PostResponse
    
    # チャンネルを取得(時間カウント対象かどうか確認 & 存在しない場合は追加)
    channel = db.select('channels', ['*'], 'id = %s',[voiceActivity.channel_id])
    

    # 最後のログを取ってくる
    lastLog = db.query('SELECT * FROM study_time WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1', [user_id])
    # ログがなかったときは累積和が0の新しいレコードを追加する
    #if len(lastLog) == 0:

    #res = db.insert('study_time', ['user_id', 'timestamp', 'status', 'cumulative_sum'], [user_id, voiceActivity.timestamp, voiceActivity.status])
    return ret