from pydantic import BaseModel

# このファイルはリクエストボディを定義するためのファイルでごわす

# user 追加リクエストの型
class PostUserAdd(BaseModel):
    discord_user_id: int

# バッジ装備リクエストの型
class PutBadgeSet(BaseModel):
    badge_1: int
    badge_2: int
    badge_3: int