import pymysql, pymysql.cursors

# MySQLとやり取りするclass。
# setterで各種必要事項をぶち込んでから使用する。
# このクラスはインスタンス化しちゃだめよ♡
class DBAccess:
    
    # クラス変数など
    __host = ''
    __port = 3306
    __db = ''
    __user = ''
    __pass = ''


    #---- setter ----#

    @classmethod
    def host(self, host): self.__host = host

    @classmethod
    def port(self, port): self.__port = port

    @classmethod
    def user(self, user): self.__user = user

    @classmethod
    def password(self, password): self.__pass = password

    @classmethod
    def database(self, db): self.__db = db


    # 接続/解放デコレータ
    def connect(func):
        def wrapper(self, *args, **kwargs):
            ret = 'error'
            connection = pymysql.connect(
                host = self.__host,
                port = self.__port,
                user = self.__user,
                password = self.__pass,
                db = self.__db,
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor)
            
            try:
                with connection.cursor() as cursor:
                    connection.begin()
                    tmp = func(self, *args, **kwargs)
                    if len(tmp) == 1: cursor.execute(tmp[0])
                    else: cursor.execute(tmp[0], tmp[1])
                    ret = cursor.fetchall()
                    connection.commit()
                
                if len(ret) == 1: ret = ret[0]

            except Exception as e:
                print('DB_ERROR:')
                print('          type:', str(type(e)))
                print('          args:', str(e.args), '\n')
                connection.rollback()
            
            finally: connection.close()
            
            return ret
        
        return wrapper
    

    # 複雑なSQLを送る必要がある場合
    @classmethod
    @connect
    def query(cls, sql, placeholder=''):
        if placeholder=='': return (sql,)
        else: return (sql, placeholder)


    # 簡易 SELECT
    @classmethod
    @connect
    def select(cls, table, column=['*'], where='', placeholder=tuple()):
        sql = 'SELECT %s FROM %s' % (', '.join(column), table)
        if placeholder == tuple(): return (sql,)
        else: return (sql + ' WHERE ' + where, placeholder)


    # 簡易 INSERT
    @classmethod
    @connect
    def insert(cls, table, column=[], values=[]):
        sql = 'INSERT INTO %s (%s) VALUE (%s)' % (table, ', '.join(column), ', '.join(['%s']*len(values)))
        return (sql, values)