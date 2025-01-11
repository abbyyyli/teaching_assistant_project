import sys
import os

# 添加專案根目錄到 Python 的模組搜索路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import pymysql
from pymysql.cursors import DictCursor
from contextlib import contextmanager
import config

@contextmanager
def get_connection():
    """
    提供 MySQL 連接的上下文管理器。
    自動處理連接的打開和關閉。
    """
    connection = pymysql.connect(
        host="localhost",
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB,
        port=config.MYSQL_PORT,
        cursorclass=DictCursor
    )
    try:
        yield connection
    finally:
        connection.close()

# ----------------------------------------
# 用戶管理功能
# ----------------------------------------

def save_user(line_user_id, name=None):
    """
    新增用戶到 users 表。
    :param line_user_id: LINE 用戶唯一 ID
    :param name: 用戶名稱 (可選)
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO users (line_user_id, name)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE name=VALUES(name)
            """
            cursor.execute(sql, (line_user_id, name))
            connection.commit()

def fetch_user(line_user_id):
    """
    根據 LINE 用戶 ID 獲取用戶資料。
    :param line_user_id: LINE 用戶唯一 ID
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE line_user_id = %s"
            cursor.execute(sql, (line_user_id,))
            return cursor.fetchone()

# ----------------------------------------
# 會話管理功能
# ----------------------------------------

def save_session(user_id, session_data):
    """
    儲存用戶會話上下文到 sessions 表。
    :param user_id: users 表中的 user_id
    :param session_data: 會話上下文（JSON 格式）
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO sessions (user_id, session_data)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (user_id, session_data))
            connection.commit()

def fetch_session(user_id):
    """
    獲取用戶當前的會話上下文。
    :param user_id: users 表中的 user_id
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                SELECT session_data
                FROM sessions
                WHERE user_id = %s
                ORDER BY created_at DESC
                LIMIT 1
            """
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            return result["session_data"] if result else None

# ----------------------------------------
# 教學內容功能
# ----------------------------------------

def save_teaching_content(user_id, topic, content):
    """
    儲存教學內容到 teaching_content 表。
    :param user_id: users 表中的 user_id
    :param topic: 教學主題
    :param content: 教學內容
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO teaching_content (user_id, topic, content)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (user_id, topic, content))
            connection.commit()

def fetch_teaching_content(user_id, topic=None):
    """
    根據用戶 ID 和主題獲取教學內容。
    :param user_id: users 表中的 user_id
    :param topic: 教學主題 (可選)
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            if topic:
                sql = """
                    SELECT *
                    FROM teaching_content
                    WHERE user_id = %s AND topic = %s
                """
                cursor.execute(sql, (user_id, topic))
            else:
                sql = """
                    SELECT *
                    FROM teaching_content
                    WHERE user_id = %s
                """
                cursor.execute(sql, (user_id,))
            return cursor.fetchall()

# ----------------------------------------
# 錯誤記錄功能
# ----------------------------------------

def log_error(user_id, error_message):
    """
    記錄錯誤信息到 error_logs 表。
    :param user_id: users 表中的 user_id (可選)
    :param error_message: 錯誤描述
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO error_logs (user_id, error_message)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (user_id, error_message))
            connection.commit()

# ----------------------------------------
# 測驗結果功能
# ----------------------------------------

def save_quiz_result(user_id, quiz_data, score):
    """
    儲存用戶測驗結果到 quiz_results 表。
    :param user_id: users 表中的 user_id
    :param quiz_data: 測驗內容（JSON 格式）
    :param score: 測驗得分
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO quiz_results (user_id, quiz_data, score)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (user_id, quiz_data, score))
            connection.commit()

def fetch_quiz_results(user_id):
    """
    獲取用戶所有測驗結果。
    :param user_id: users 表中的 user_id
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            sql = """
                SELECT *
                FROM quiz_results
                WHERE user_id = %s
            """
            cursor.execute(sql, (user_id,))
            return cursor.fetchall()

# ----------------------------------------
# 測試代碼
# ----------------------------------------

if __name__ == "__main__":
    # 測試用戶新增
    save_user("U12345", "Abby")
    user = fetch_user("U12345")
    print("Fetched User:", user)

    # 測試教學內容保存和查詢
    save_teaching_content(user["id"], "Python Basics", "This is a Python tutorial.")
    content = fetch_teaching_content(user["id"], "Python Basics")
    print("Teaching Content:", content)

    # 測試記錄錯誤
    log_error(user["id"], "Sample error message")
