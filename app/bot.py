from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from utils.redis_manager import RedisManager
from handlers.message_handler import handle_text_message

app = Flask(__name__)

# LINE API credentials (use environment variables)
import config
line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

# Redis for session management
redis_manager = RedisManager()

@app.route("/callback", methods=["POST"])
def callback():
    # Get LINE signature header
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return "Invalid signature", 400

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_message = handle_text_message(user_message, redis_manager)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

if __name__ == "__main__":
    app.run(port=5000)
