import redis
import json

class RedisManager:
    def __init__(self, host="localhost", port=6379, db=0):
        """
        初始化 Redis 客戶端。
        :param host: Redis 伺服器地址
        :param port: Redis 伺服器埠
        :param db: 使用的資料庫
        """
        self.redis_client = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            decode_responses=True  # 自動解碼 UTF-8 字符串
        )

    def save_session_data(self, user_id, data):
        """
        保存用戶的會話上下文。
        :param user_id: 唯一用戶 ID
        :param data: 要保存的上下文數據（dict 格式）
        """
        session_key = f"session:{user_id}"
        self.redis_client.set(session_key, json.dumps(data))

    def get_session_data(self, user_id):
        """
        獲取用戶的會話上下文。
        :param user_id: 唯一用戶 ID
        :return: 上下文數據（dict 格式）或 None
        """
        session_key = f"session:{user_id}"
        session_data = self.redis_client.get(session_key)
        return json.loads(session_data) if session_data else None

    def delete_session_data(self, user_id):
        """
        刪除用戶的會話上下文。
        :param user_id: 唯一用戶 ID
        """
        session_key = f"session:{user_id}"
        self.redis_client.delete(session_key)

print("i love u")