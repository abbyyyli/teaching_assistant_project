import sys
import os

# 將專案根目錄加入模組搜索路徑
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
from unittest.mock import patch, MagicMock
from app.bot import app

class TestBot(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch("linebot.v3.WebhookHandler.handle")
    def test_webhook_valid_signature(self, mock_handle):
        """
        測試有效的 LINE 簽名是否處理成功。
        """
        # 模擬處理函數成功執行
        mock_handle.return_value = None

        response = self.app.post(
            "/callback",
            headers={"X-Line-Signature": "valid_signature"},
            data='{"events": [{"type": "message", "message": {"type": "text", "text": "start"}}]}'
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
