import pymysql
from pymysql.cursors import DictCursor
from contextlib import contextmanager
import config

@contextmanager
def get_connection():
    """
    管理 MySQL 連接的上下文管理器。
    """
    connection = pymysql.connect(
        host="localhost",
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB,
        cursorclass=DictCursor,
    )
    try:
        yield connection
    finally:
        connection.close()

def fetch_all_users():
    """
    獲取所有用戶的數據。
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            return cursor.fetchall()

# 測試用例
if __name__ == "__main__":
    users = fetch_all_users()
    print("Users:", users)
