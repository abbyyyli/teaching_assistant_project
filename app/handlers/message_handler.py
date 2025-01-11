from utils.llm_connector import llm_connector
from utils.redis_manager import RedisManager

def handle_text_message(user_id, message, redis_manager: RedisManager):
    """
    處理用戶的文本消息並生成相應的回覆。
    :param user_id: LINE 用戶的唯一 ID
    :param message: 用戶輸入的消息
    :param redis_manager: Redis 管理對象，用於上下文管理
    :return: 回覆用戶的消息
    """
    # 獲取用戶上下文狀態
    session_data = redis_manager.get_session_data(user_id) or {"state": "start"}

    # 狀態機：根據當前狀態處理消息
    state = session_data.get("state")

    if state == "start":
        # 初始狀態
        redis_manager.save_session_data(user_id, {"state": "teaching"})
        return "Welcome! Please provide a topic to start teaching."

    elif state == "teaching":
        # 教學內容生成
        teaching_content = llm_connector.generate_response(f"Generate teaching content on: {message}")
        redis_manager.save_session_data(user_id, {"state": "quiz", "topic": message})
        return f"Teaching Content:\n{teaching_content}"

    elif state == "quiz":
        # 測驗問題生成
        topic = session_data.get("topic", "this topic")
        quiz_content = llm_connector.generate_response(f"Generate a quiz for the topic: {topic}.")
        redis_manager.save_session_data(user_id, {"state": "feedback", "topic": topic})
        return f"Quiz for {topic}:\n{quiz_content}"

    elif state == "feedback":
        # 反饋生成
        topic = session_data.get("topic", "this topic")
        feedback = llm_connector.generate_response(f"Provide feedback for the quiz on: {topic}.")
        redis_manager.save_session_data(user_id, {"state": "completed"})
        return f"Feedback for {topic}:\n{feedback}"

    elif state == "completed":
        # 對話完成狀態
        redis_manager.delete_session_data(user_id)
        return "The session is completed. Type 'start' to begin a new session."

    else:
        # 未知狀態
        return "I'm sorry, I didn't understand your message. Type 'start' to begin."

