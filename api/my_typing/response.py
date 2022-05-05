from typing import Optional, List
from pydantic import BaseModel

# ---- ベース ---- #

# エラー情報
class Error(BaseModel):
    error_code: int = 0
    message: Optional[str] = 'this is default message.'

    # 正常終了コードをセットする
    def success(self):
        self.error_code = 0
        self.message = 'success'
    
    # 異常終了コードをセットする
    def error(self, message = ''):
        self.error_code = 1
        if message != '': self.message = message

# 戻り値のベース
class ResponseBase(BaseModel):
    error: Error = Error()


# ---- 戻り値の定義 ---- #

# ユーザーの設定
class BaseUserSettings(BaseModel):
    privacy_data: bool = False
    privacy_rank: bool = False

# ユーザー
class BaseUser(BaseModel):
    id: int = 0
    settings: BaseUserSettings = BaseUserSettings()

# guild
class BaseGuild(BaseModel):
    id: int
    study_rooms: tuple
    auto_role: bool
    global_ranking: bool

# 自習ランク
class BaseRank(BaseModel):
    id: int
    name: str
    description: str
    color: str
    condition: int

# バッジ
class BaseBadge(BaseModel):
    id: int = 0
    name: str = 'badge name'
    description: str = 'description of this badge.'

# 自習時間(1行)
class BaseStudyTimeOneLine(BaseModel):
    id: int
    user_id: int
    timestamp: int
    status: bool
    cumulative_sum: int

# ranking(1行)
class BaseRankingOneLine(BaseModel):
    user_id: int
    time: int


# ---- apiの実際のレスポンス ---- #

# ユーザー
class User(ResponseBase):
    body: BaseUser = BaseUser()

# guild
class Guild(ResponseBase):
    body: BaseGuild

# 自習ランク
class Rank(ResponseBase):
    body: BaseRank

# バッジ
class Badge(ResponseBase):
    body: BaseBadge

# バッジ(複数)
class Badges(ResponseBase):
    body: List[BaseBadge] = []

    # バッジ情報をbodyに追加
    def appendBadge(self, id, name, description):
        self.body.append(BaseBadge(id=id, name=name, description=description))


# 自習時間
class StudyTime(ResponseBase):
    body: List[BaseStudyTimeOneLine] = []

# ランキング
class Ranking(ResponseBase):
    body: List[BaseRankingOneLine] = []


# POST の戻り値用エイリアス
PostResponse = ResponseBase

# PUT の戻り値用エイリアス
PutResponse = ResponseBase