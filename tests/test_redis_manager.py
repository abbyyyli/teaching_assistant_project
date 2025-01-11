import sys
import os

# 將專案根目錄加入模組搜索路徑
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import unittest
from app.utils.redis_manager import RedisManager

class TestRedisManager(unittest.TestCase):
    def setUp(self):
        """
        初始化 Redis 連接。
        """
        self.redis_manager = RedisManager(host="localhost", port=6379, db=0)

    def test_save_and_fetch_session(self):
        """
        測試保存和獲取會話數據。
        """
        user_id = "test_user"
        session_data = {"state": "teaching", "topic": "Python"}

        # 保存數據
        self.redis_manager.save_session_data(user_id, session_data)

        # 獲取數據
        fetched_data = self.redis_manager.get_session_data(user_id)
        self.assertEqual(fetched_data, session_data)

    def test_delete_session(self):
        """
        測試刪除會話數據。
        """
        user_id = "test_user"
        session_data = {"state": "teaching"}

        # 保存數據
        self.redis_manager.save_session_data(user_id, session_data)

        # 刪除數據
        self.redis_manager.delete_session_data(user_id)
        fetched_data = self.redis_manager.get_session_data(user_id)
        self.assertIsNone(fetched_data)

if __name__ == "__main__":
    unittest.main()
