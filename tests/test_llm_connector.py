print("Running tests in test_llm_connector.py")


import sys
import os

# 將專案根目錄加入模組搜索路徑
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
from unittest.mock import patch, MagicMock
from app.utils.llm_connector import LLMConnector

class TestLLMConnector(unittest.TestCase):
    def setUp(self):
        """
        初始化測試環境。
        """
        self.llm_connector = LLMConnector(model="gpt-4", temperature=0.7)

    @patch("app.utils.llm_connector.ChatOpenAI")
    def test_generate_response_success(self, mock_chat_openai):
        """
        測試 LLM 成功回應。
        """
        # 模擬 LLM 回應
        mock_client = MagicMock()
        mock_client.predict.return_value = "This is a test response."
        mock_chat_openai.return_value = mock_client

        prompt = "What is the capital of France?"
        response = self.llm_connector.generate_response(prompt)
        self.assertEqual(response, "This is a test response.")

    @patch("app.utils.llm_connector.ChatOpenAI")
    def test_generate_response_error(self, mock_chat_openai):
        """
        測試 LLM 回應錯誤情況。
        """
        # 模擬 LLM 出錯
        mock_client = MagicMock()
        mock_client.predict.side_effect = Exception("LLM error occurred.")
        mock_chat_openai.return_value = mock_client

        prompt = "What is the capital of France?"
        response = self.llm_connector.generate_response(prompt)
        self.assertEqual(response, "Error querying LLM: LLM error occurred.")

if __name__ == "__main__":
    unittest.main()

