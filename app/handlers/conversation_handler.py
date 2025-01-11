from app.utils.prompt_loader import PromptLoader
from app.utils.state_manager import StateManager

class ConversationHandler:
    def __init__(self):
        self.prompt_loader = PromptLoader()
        self.state_manager = StateManager()

    def handle_input(self, user_input):
        """
        根據用戶輸入和當前狀態處理回應
        :param user_input: 用戶輸入
        :return: 系統回應
        """
        state, user_data = self.state_manager.get_current_state()

        if state == "awaiting_topic":
            self.state_manager.update_state("generating_content", {"topic": user_input})
            template = self.prompt_loader.load_prompt("templates")["teaching_template"]
            return template.format(topic=user_input)

        elif state == "generating_content":
            teaching_content = f"Generated teaching content about {user_data['topic']}."
            self.state_manager.update_state("awaiting_feedback")
            return teaching_content

        elif state == "awaiting_feedback":
            return "Thank you for your feedback!"

        else:
            return "Unknown state. Please try again."
