import unittest
from app.bot import app

class BotTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_callback_invalid_signature(self):
        response = self.app.post("/callback", headers={"X-Line-Signature": "invalid"}, data="test")
        self.assertEqual(response.status_code, 400)

    def test_callback_valid_signature(self):
        # Mock signature and body for a valid request (add your logic here)
        pass

if __name__ == "__main__":
    unittest.main()

