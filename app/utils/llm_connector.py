import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class LLMConnector:
    def __init__(self, model="gpt-4", temperature=0.7):
        """
        初始化 LLM 客戶端
        :param model: 使用的模型名稱（如 gpt-3.5-turbo 或 gpt-4）
        :param temperature: 控制生成的隨機性
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in environment variables!")
        
        self.client = ChatOpenAI(
            model=model,
            temperature=temperature,
            openai_api_key=api_key
        )

    def generate_response(self, prompt: str) -> str:
        """
        發送 Prompt 到 LLM 並獲取結果
        :param prompt: 用戶輸入的文字
        :return: LLM 回應的純文字
        """
        try:
            response = self.client.invoke(prompt)  # 獲取 AIMessage 對象
            return response.content  # 提取純文字內容
        except Exception as e:
            return f"Error querying LLM: {str(e)}"
