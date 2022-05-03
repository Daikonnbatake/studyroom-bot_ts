from pydantic import BaseModel

# このファイルはリクエストボディを定義するためのファイルでごわす

# user 追加リクエストの型
class PostUserAdd(BaseModel):
    discord_user_id: int
    