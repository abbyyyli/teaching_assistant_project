class StateManager:
    def __init__(self):
        self.state = "awaiting_topic"  # 初始狀態
        self.user_data = {}           # 用戶特定數據（如主題）

    def update_state(self, new_state, data=None):
        """
        更新狀態
        :param new_state: 新狀態
        :param data: 可選的額外數據
        """
        self.state = new_state
        if data:
            self.user_data.update(data)

    def get_current_state(self):
        """
        獲取當前狀態
        """
        return self.state, self.user_data
