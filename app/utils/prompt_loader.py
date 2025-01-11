import json
from pathlib import Path

class PromptLoader:
    def __init__(self, folder="app/prompts"):
        """
        初始化 Prompt Loader
        :param folder: 存放模板的資料夾路徑
        """
        self.folder = Path(folder)

    def load_prompt(self, template_name):
        """
        加載指定模板
        :param template_name: 模板名稱（不含後綴）
        :return: 模板內容
        """
        path = self.folder / f"{template_name}.json"
        if not path.exists():
            raise FileNotFoundError(f"Prompt template {template_name}.json not found in {self.folder}")
        with open(path, "r") as file:
            return json.load(file)
