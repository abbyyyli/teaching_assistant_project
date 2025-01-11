import unittest
from app.handlers.conversation_handler import ConversationHandler

class TestConversationHandler(unittest.TestCase):
    def setUp(self):
        self.handler = ConversationHandler()

    def test_topic_input(self):
        response = self.handler.handle_input("Python Basics")
        self.assertIn("Explain the topic: Python Basics", response)

    def test_generate_content(self):
        self.handler.handle_input("Python Basics")
        response = self.handler.handle_input("")
        self.assertIn("Generated teaching content about Python Basics.", response)
