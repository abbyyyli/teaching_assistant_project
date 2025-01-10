from utils.llm_connector import query_openai_llm

def handle_text_message(message, redis_manager):
    # Check if session exists in Redis
    session_data = redis_manager.get_session_data(user_id="example_user_id")

    if message.lower() == "start":
        redis_manager.save_session_data(user_id="example_user_id", data={"state": "teaching"})
        return "Welcome! Please provide a topic to start teaching."

    # If state is "teaching," generate teaching content
    if session_data and session_data.get("state") == "teaching":
        teaching_content = query_openai_llm(f"Generate teaching content on {message}")
        return f"Teaching Content: {teaching_content}"

    return "I'm sorry, I didn't understand your message."
