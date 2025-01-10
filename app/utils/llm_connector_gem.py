import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 加載環境變數
load_dotenv()

# 從環境變數獲取 Gemini API Key
GEMINI_API_KEY= "AIzaSyBfSKLS0lW41qUtxVwaNcz-Yln1qIIIhzY"


# 初始化 Gemini LLM，禁用默認憑證
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    googleapikey=GEMINI_API_KEY,
    credentials=None  # 禁用 Application Default Credentials
)

def query_gemini_llm(prompt: str) -> str:
    """
    發送 Prompt 到 Gemini LLM 並獲取結果。
    """
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error querying Gemini LLM: {str(e)}"

# 測試用例
if __name__ == "__main__":
    test_prompts = ["What is the capital of France?"]
    for prompt in test_prompts:
        result = query_gemini_llm(prompt)
        print(f"Prompt: {prompt}\nResponse: {result}\n")
