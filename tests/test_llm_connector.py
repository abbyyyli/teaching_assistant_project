import unittest
from app.utils.llm_connector import query_openai_llm

class TestLLMConnector(unittest.TestCase):
    def test_query_openai_llm(self):
        prompt = "What is the capital of France?"
        response = query_openai_llm(prompt)
        self.assertIn("Paris", response, "LLM response does not contain the expected answer.")

if __name__ == "__main__":
    unittest.main()
