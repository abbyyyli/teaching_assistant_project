import hmac
import hashlib
import base64

# Replace with your Channel Secret
CHANNEL_SECRET = "975d7aa8bdc06899a4ac5567cb9e31eb"

# Replace with your request body
body = '''{
    "events": [
        {
            "type": "message",
            "message": {
                "type": "text",
                "text": "Hello, bot!"
            },
            "replyToken": "dummy-reply-token"
        }
    ]
}'''

# Generate the signature
hash = hmac.new(CHANNEL_SECRET.encode('utf-8'), body.encode('utf-8'), hashlib.sha256)
signature = base64.b64encode(hash.digest()).decode('utf-8')

print(f"Signature: {signature}")
